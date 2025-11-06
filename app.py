import os
from flask import Flask, request, send_file, jsonify
from rembg import remove
from PIL import Image
from io import BytesIO

app = Flask(__name__)

# Rota de saúde para o Render
@app.route('/')
def health_check():
    return jsonify({"status": "ok", "service": "rembg-api"})

@app.route('/remove', methods=['POST'])
def remove_background():
    # 1. Verificar se o arquivo foi enviado
    if 'file' not in request.files:
        return jsonify({"error": "Nenhum arquivo 'file' na requisição."}), 400

    file = request.files['file']
    
    # 2. Verificar se o nome do arquivo está vazio
    if file.filename == '':
        return jsonify({"error": "Nenhum arquivo selecionado."}), 400

    # 3. Processar a imagem
    try:
        # Abrir a imagem com PIL
        input_image = Image.open(file.stream)
        
        # Remover o fundo
        output_image = remove(input_image)
        
        # Salvar a imagem processada em um buffer de bytes
        byte_io = BytesIO()
        output_image.save(byte_io, 'PNG')
        byte_io.seek(0)
        
        # 4. Retornar a imagem
        return send_file(
            byte_io,
            mimetype='image/png',
            as_attachment=True,
            download_name='no-bg.png'
        )

    except Exception as e:
        # 5. Lidar com erros de processamento
        print(f"Erro durante o processamento: {e}")
        return jsonify({"error": f"Erro interno ao processar a imagem: {str(e)}"}), 500

if __name__ == '__main__':
    # Usar a porta fornecida pelo Render (ou 5000 como fallback)
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
