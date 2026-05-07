cat > README.md << 'EOF'
# Calculateur d'IMC - Application Dockerisée

## 📋 Informations générales

| Élément | Détail |
|---------|--------|
| **Titre du projet** | Calculateur d'IMC (Indice de Masse Corporelle) |
| **Auteur** | deslannnnnnnd |
| **Date de remise** | 08 mai 2026 |
| **Validation en classe** | 12 mai 2026 |
| **Technologies** | Python 3.11, Flask 2.3.3, Docker, Docker Compose |
| **Dépôt GitHub** | https://github.com/deslannnnnnnd/projet-docker-imc |

---

## 🎯 Description du projet

Application web simple de calcul d'IMC conteneurisée avec Docker.

**Fonctionnalité :** L'utilisateur entre son poids (kg) et sa taille (m), l'application calcule son IMC et affiche la catégorie correspondante.

### Formule de calcul


### Catégories d'IMC

| IMC | Catégorie |
|-----|-----------|
| Moins de 18,5 | Maigreur |
| 18,5 – 24,9 | Normal |
| 25 – 29,9 | Surpoids |
| 30 et plus | Obésité |

---

## 🏗️ Architecture du projet

### Structure des fichiers
projet-docker-imc/
└── projet_docker/
├── app.py # Application Flask
├── Dockerfile # Configuration Docker
├── docker-compose.yml # Orchestration
├── requirements.txt # Dépendances Python
└── README.md # Documentation


### Rôle de chaque fichier

| Fichier | Description |
|---------|-------------|
| `app.py` | Code source de l'application Flask avec interface HTML |
| `Dockerfile` | Instructions pour construire l'image Docker |
| `docker-compose.yml` | Configuration simplifiée du lancement |
| `requirements.txt` | Liste des dépendances (flask==2.3.3) |

---

## 🐳 Docker : Image et Conteneur

| Concept | Explication |
|---------|-------------|
| **Image Docker** | Modèle/recette contenant Python, Flask et le code |
| **Conteneur** | Instance réelle de l'application en cours d'exécution |

### Contenu du Dockerfile
```dockerfile
FROM python:3.11-slim    # Image de base légère
WORKDIR /app              # Dossier de travail dans le conteneur
COPY requirements.txt .   # Copie des dépendances
RUN pip install --no-cache-dir -r requirements.txt  # Installation Flask
COPY app.py .             # Copie de l'application
EXPOSE 5000               # Port utilisé par l'application
CMD ["python", "app.py"]  # Commande de démarrage
