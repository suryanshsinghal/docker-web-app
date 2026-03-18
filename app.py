from flask import Flask, jsonify
import datetime
import socket
import os

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>🚀 Dockerized Flask App</h1>
    <p>Status: <b>Running Successfully</b></p>
    <p>Welcome to a containerized web application deployed on cloud.</p>
    """

@app.route('/health')
def health():
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.datetime.now().isoformat()
    })

@app.route('/info')
def info():
    return jsonify({
        "hostname": socket.gethostname(),
        "ip_address": socket.gethostbyname(socket.gethostname()),
        "environment": os.getenv("ENV", "development"),
        "version": "1.0.0"
    })

@app.route('/about')
def about():
    return """
    <h2>About This Project</h2>
    <ul>
        <li>Built using Flask</li>
        <li>Containerized using Docker</li>
        <li>Deployed on AWS EC2</li>
    </ul>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)