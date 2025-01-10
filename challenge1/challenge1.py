from flask import Flask, request
from datetime import datetime
import socket

app = Flask(__name__)

@app.route("/")
def hello_world():
    server_ip = request.host_url
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"""
    <div style="text-align: center">
        <h1>Rjiba Ilef</h1>
        <h2>Project: <b>Challenge 1</b></h2>
        <p>Version: <b>V1</b></p>
        <p>Server Hostname: <b>{server_ip}</b></p>
        <p>Current Date: <b>{current_date}</b></p>
    </div>
    """
if __name__== "_main_":
   app.run(host="0.0.0.0", port=5000)