# Use a imagem oficial do Python
FROM python:3.12-slim

# Define o diretório de trabalho no contêiner
WORKDIR /app

# Copia o arquivo requirements.txt para o contêiner
COPY requirements.txt .

# Instala as dependências
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copia todo o conteúdo do diretório atual para o contêiner no diretório /app
COPY . .

# Comando padrão a ser executado quando um contêiner baseado nessa imagem for iniciado
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
