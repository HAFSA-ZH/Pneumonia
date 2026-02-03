# Utiliser une image Python slim pour réduire la taille
FROM python:3.12-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier uniquement les fichiers nécessaires
COPY requirements.txt .
COPY app.py .   # Remplace par le nom de ton fichier principal si différent
# COPY autres fichiers nécessaires
# COPY dossiers si besoin

# Installer les dépendances sans cache pour réduire la taille
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Exposer le port utilisé par Flask
EXPOSE 5000

# Commande pour lancer ton application
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
