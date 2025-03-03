from flask import Flask, request, jsonify
from gradio_client import Client

app = Flask(__name__)
client = Client("malavikaaaaaaaaaaaaa/sm")

# Health check or welcome route
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Server is running! Use the /predict endpoint to send requests."})

# Prediction route (POST)
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    username = data.get("username")
    name_or_relation = data.get("name_or_relation")
    
    if not username or not name_or_relation:
        return jsonify({"error": "Missing username or name_or_relation"}), 400
    
    result = client.predict(
        username=username,
        name_or_relation=name_or_relation,
        api_name="/predict"
    )
    
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)
