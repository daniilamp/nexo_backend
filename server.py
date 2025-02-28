from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Backend funcionando en Railway 🚀"

@app.route("/health")
def health_check():
    return "OK", 200  # Asegúrate de que esta línea tiene 4 espacios de indentación

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

