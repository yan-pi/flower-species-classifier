# Usa uma imagem base oficial do Python
FROM python:3.8-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos necessários
COPY requirements.txt requirements.txt
COPY main.py main.py
COPY model.pkl model.pkl

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta
EXPOSE 5000

# Comando para rodar a aplicação
CMD ["python", "main.py"]
