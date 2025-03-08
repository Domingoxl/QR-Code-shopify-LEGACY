from flask import Flask, render_template
import os

app = Flask(__name__, template_folder='server/templates')  # Update the path
import os
print("Looking for templates in:", os.path.abspath(os.path.join(os.path.dirname(__file__), 'templates')))

@app.route('/', methods=['GET', 'HEAD'])
def home():
    return render_template('index.html')

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
