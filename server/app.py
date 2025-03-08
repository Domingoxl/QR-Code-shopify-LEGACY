from flask import Flask, render_template
import os
print("Template Directory:", os.path.abspath(os.path.join(os.path.dirname(__file__), 'templates')))
app = Flask(__name__, template_folder='server/templates')
@app.route('/', methods=['GET', 'HEAD'])
def home():
    return render_template('index.html')
if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))  # Ensure Flask uses the correct port
    app.run(host="0.0.0.0", port=port)
