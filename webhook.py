from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route("/alert", methods=['POST'])
def alerts():
    data = request.json
    print(data, flush=True)
    if data.get("status") == "firing":
        subprocess.run(["ansible-playbook", "-i", "inventory.ini", "restart-nginx.yml"])
    return "ok"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
