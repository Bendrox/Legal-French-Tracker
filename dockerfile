# Utiliser une image Python comme base
FROM python:3.13.1

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de l'app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# Expose le port utilisé 
EXPOSE 8501

# Lancer l’application
CMD ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]