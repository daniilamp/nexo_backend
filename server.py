from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Backend funcionando en Railway 🚀"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))  # Usa el puerto que Railway asigna
    app.run(host="0.0.0.0", port=port)