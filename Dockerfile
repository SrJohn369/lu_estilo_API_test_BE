# Use a imagem oficial do Python
FROM python:3.12-slim

# Define o diretório de trabalho no contêiner
WORKDIR /app

# Copia o arquivo requirements.txt para o contêiner
COPY requirements.txt .

# Instala as dependências
RUN pip install -r requirements.txt

# Copia todo o conteúdo do diretório atual para o contêiner no diretório /app
COPY . .

# Define o comando de inicialização do contêiner usando um script
CMD ["bash", "./start.sh"]
