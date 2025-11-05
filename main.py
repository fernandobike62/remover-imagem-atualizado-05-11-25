import os
from flask import Flask, request, Response
from rembg import remove
from flask_cors import CORS

API_KEY = os.getenv("API_KEY")

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return {"message": "✅ API Remover Fundo ativa e funcionando!"}

@app.route("/remove-bg", methods=["POST"])
def remove_bg():
    auth = request.headers.get("Authorization")
    if API_KEY and auth != f"Bearer {API_KEY}":
        return {"error": "Acesso não autorizado"}, 401

    if 'file' not in request.files:
        return {"error": "Nenhum arquivo enviado"}, 400

    f = request.files['file']
    input_bytes = f.read()

    try:
        output_bytes = remove(input_bytes)
    except Exception as e:
        return {"error": f"Erro ao remover fundo: {str(e)}"}, 500

    return Response(output_bytes, mimetype="image/png")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
