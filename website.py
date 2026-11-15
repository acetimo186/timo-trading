# website.py - DO NOT paste HTML here. This file only SERVES index.html
from flask import Flask, send_file
import os

app = Flask(__name__)

@app.route("/")
def home():
    # Serves your TIMO site
    if os.path.exists("index.html"):
        return send_file("index.html")
    return "index.html not found - please upload index.html next to website.py"

@app.route("/<path:path>")
def static_files(path):
    if os.path.exists(path):
        return send_file(path)
    return "Not found", 404

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
