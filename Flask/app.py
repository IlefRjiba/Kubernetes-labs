from flask import Flask, request
from datetime import datetime
import socket
import os
from pymongo import MongoClient

app = Flask(__name__)

MONGO_URL = os.getenv("MONGO_URL")
mongo_client = MongoClient(MONGO_URL)
db = mongo_client["flask_db"]  
collection = db["requests"]  

@app.route("/")
def hello_world():
    server_ip = request.host_url

    hostname = socket.gethostname()
    
    client_ip = request.remote_addr

    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    collection.insert_one({"client_ip": client_ip, "date": current_date})

    last_records = collection.find().sort("_id", -1).limit(10)

    records_html = "<ul>"
    for record in last_records:
        records_html += f"<li>IP: {record['client_ip']} | Date: {record['date']}</li>"
    records_html += "</ul>"

    return f"""
    <div style="text-align: center">
        <h1>Bentaleb Ali Ahmed</h1>
        <h2>Project: <b>Kubernetes Project</b></h2>
        <p>Version: <b>V2</b></p>
        <p>Server Hostname: <b>{hostname}</b></p>
        <p>Current Date: <b>{current_date}</b></p>
        <h2>Last 10 Requests:</h2>
        {records_html}
    </div>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
