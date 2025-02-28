import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Backend funcionando en Railway 🚀"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))  # Toma el puerto de Railway o usa 8080 por defecto
    app.run(host="0.0.0.0", port=port)