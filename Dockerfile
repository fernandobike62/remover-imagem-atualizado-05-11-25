# Use uma imagem base Python
FROM python:3.10-slim

# Definir o diretório de trabalho
WORKDIR /app

# Instalar dependências do sistema necessárias para rembg
# O rembg requer libgl1-mesa-glx para algumas operações
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

# Copiar os arquivos de dependência e instalar
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código do aplicativo
COPY . .

# Expor a porta que o Flask usará (Render injeta a variável PORT)
EXPOSE 5000

# Comando para iniciar o servidor com Gunicorn
# A variável de ambiente PORT será injetada pelo Render
CMD ["gunicorn", "--bind", "0.0.0.0:$PORT", "app:app"]
