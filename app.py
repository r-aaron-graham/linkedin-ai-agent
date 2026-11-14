"""Local reviewer fixture for the LinkedIn workflow prototype."""

from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/")
def home():
    return "LinkedIn AI Agent reviewer demo"


@app.post("/start-agent")
def start_agent():
    return jsonify(status="simulated")


@app.get("/log")
def get_log():
    return jsonify(log=["Sample log entry 1", "Sample log entry 2"])


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
