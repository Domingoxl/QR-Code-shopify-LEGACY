import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "QR Code Memorial App Running!"

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))  # Default to 5000 if PORT is not set
    app.run(host="0.0.0.0", port=port)
