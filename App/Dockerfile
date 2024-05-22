# Utilise l'image officielle Python comme base
FROM python:3.9-slim

# Définit le répertoire de travail dans le conteneur
WORKDIR /app

# Copie le fichier requirements.txt dans le répertoire de travail
COPY requirements.txt .

# Installe les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copie le contenu du répertoire de l'application dans le conteneur
COPY . .

# Expose le port que l'application Flask utilise
EXPOSE 5000

# Commande pour exécuter l'application
CMD ["python", "app.py"]