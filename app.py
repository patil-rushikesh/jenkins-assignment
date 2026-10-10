from flask import Flask, jsonify
from datetime import datetime, timezone

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify(
        message="Welcome to Flask API",
        version="1.0.0"
    )

@app.route("/health")
def health():
    return jsonify(
        status="healthy",
        timestamp=datetime.now(timezone.utc).isoformat()
    )

@app.route("/ready")
def ready():
    return jsonify(
        status="ready",
        service="flask-api"
    )

@app.errorhandler(404)
def not_found(error):
    return jsonify(error="Endpoint not found"), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6000)