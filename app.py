from flask import Flask, jsonify
from snort_log_reader import read_alerts

app = Flask(_name_)

@app.route("/alerts")
def alerts():
    return jsonify(read_alerts("/var/log/snort/alert"))  # Snort log path

app.run(host="0.0.0.0", port=5000)
