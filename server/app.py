from flask import Flask, render_template
import os

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'HEAD'])
def home():
    return render_template('index.html')


if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))  # Ensure Flask uses the correct port
    app.run(host="0.0.0.0", port=port)
