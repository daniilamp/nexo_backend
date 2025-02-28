from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/datos', methods=['POST'])
def recibir_datos():
    """Recibe datos del EA y los almacena temporalmente"""
    data = request.get_json()
    if data:
        print(f"Datos recibidos: {data}")
        return jsonify({"status": "ok", "message": "Datos guardados"}), 200
    return jsonify({"status": "error", "message": "Datos inválidos"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
