from flask import Flask, render_template
import os

# Ensure Flask looks for templates in the correct directory
app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), "templates"))

@app.route('/', methods=['GET', 'HEAD'])
def home():
  return "<h1>QR Code Memorial App Running Successfully!</h1>"


if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))  # Ensure Flask uses the correct port
    app.run(host="0.0.0.0", port=port)
