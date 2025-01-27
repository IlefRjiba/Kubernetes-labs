from flask import Flask, request
from datetime import datetime
import socket
import os

app = Flask(__name__)

@app.route("/")
def hello_world():
    server_ip = request.host_url

    hostname = socket.gethostname()
    
    client_ip = request.remote_addr

    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return f"""
    <div style="text-align: center">
        <h1>Rjiba Ilef</h1>
        <h2>Project: <b>Kubernetes Project: webnodb</b></h2>
        <p>Version: <b>V2</b></p>
        <p>Server Hostname: <b>{hostname}</b></p>
        <p>Current Date: <b>{current_date}</b></p>
    </div>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
