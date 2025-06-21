# app.py
from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    # Get a message from an environment variable, or use a default
    message = os.environ.get("HELLO_MESSAGE", "Hello from Azure Kubernetes Service!")
    return f"<h1>{message}</h1>"

if __name__ == '__main__':
    # Run on all available interfaces, port 5000 (standard for Flask)
    app.run(host='0.0.0.0', port=5000)
