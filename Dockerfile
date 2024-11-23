# Dockerfile

# Utiliser une image Python officielle comme base
FROM python:3.9-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers nécessaires
COPY requirements.txt ./
COPY app.py ./

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Exécuter le programme
CMD ["python", "app.py"]
