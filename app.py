import io
from flask import Flask, request, send_file
from rembg import remove
from PIL import Image

app = Flask(__name__)

@app.route('/remove-bg', methods=['POST'])
def remove_background():
    if 'file' not in request.files:
        return "Nenhum arquivo enviado", 400

    file = request.files['file']
    
    # Abrir a imagem
    try:
        input_image = Image.open(file.stream)
    except Exception as e:
        return f"Erro ao abrir a imagem: {e}", 400
    
    # Remover o fundo
    try:
        # O modelo padrão (u2net) é usado
        output_image = remove(input_image)
    except Exception as e:
        return f"Erro ao processar a imagem com rembg: {e}", 500
    
    # Salvar a imagem de saída em um buffer
    output_buffer = io.BytesIO()
    # O formato PNG é essencial para manter a transparência
    output_image.save(output_buffer, format='PNG')
    output_buffer.seek(0)
    
    # Retornar a imagem processada
    return send_file(
        output_buffer,
        mimetype='image/png',
        as_attachment=False,
        download_name='sem_fundo.png'
    )

if __name__ == '__main__':
    # Render usa a variável de ambiente PORT
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
