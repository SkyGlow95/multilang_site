# Multilang Site

Ce projet est un site web multilingue développé avec Django. Il inclut des fonctionnalités comme un éditeur de texte enrichi (CKEditor) et une intégration avec l'API OpenAI.

## Prérequis

Avant de commencer, assurez-vous d'avoir installé les logiciels suivants sur votre machine :

- Python 3.11
- pip (gestionnaire de paquets Python)
- Git

## Installation

1. **Cloner le dépôt :**

   ```sh
   git clone https://github.com/SkyGlow95/multilang_site.git
   cd multilang_site
   
2. **Créer et activer un environnement virtuel :**

   ```sh
   python -m venv venv
   source venv/bin/activate  # Sur Windows, utilisez `venv\Scripts\activate`

3. **Installer les dépendances :**

   ```sh
   pip install -r requirements.txt

## Configuration

1. **Paramètres Django :**

   Ouvrez le fichier settings.py et assurez-vous d'ajouter votre domaine à ALLOWED_HOSTS et CSRF_TRUSTED_ORIGINS :

   ```sh
   ALLOWED_HOSTS = ['votre-url.com', 'localhost', '127.0.0.1']
   CSRF_TRUSTED_ORIGINS = ['https://votre-url.com']

2. **Migrations de la base de données :**

   Appliquez les migrations de la base de données :

   ```sh
   python manage.py migrate

3. **Collecte des fichiers statiques :**

   Collectez les fichiers statiques :

   ```sh
   python manage.py collectstatic --noinput

## Exécution du projet

1. **Lancer le serveur de développement :**

   Pour lancer le serveur de développement, utilisez la commande suivante :

   ```sh
   python manage.py runserver

Vous devriez maintenant pouvoir accéder au site web à l'adresse http://127.0.0.1:8000/.

2. **Déploiement avec Gunicorn :**

   Pour exécuter le projet en production avec Gunicorn, utilisez la commande suivante :

   ```sh
   gunicorn multilang_site.wsgi:application --bind 0.0.0.0:8000

## Déploiement sur Render.com :

Pour déployer ce projet sur Render.com, suivez ces étapes :

1. **Connectez votre dépôt GitHub au service Render.**

2. **Configurez les variables d'environnement nécessaires dans le tableau de bord Render.**

   Pour utiliser les outils RAG et LLM vous devez inclure votre clé CHATGPT API (key = OPENAI_API_KEY) et (value = votr_clé)

4. **Ajoutez les commandes de build et de démarrage dans Render :**
   
   ```sh   
   pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate```

5. **Ajoutez les commandes de démarrage dans Render :**

   ```sh
   gunicorn multilang_site.wsgi:application --bind 0.0.0.0:8000

## Contribution

Les contributions sont les bienvenues ! Veuillez ouvrir une issue ou soumettre une pull request pour tout changement majeur.

## Licence

Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.

Ce fichier `README.md` fournit des instructions claires pour cloner, installer, configurer, et exécuter le projet, ainsi que des informations sur le déploiement et la contribution.
