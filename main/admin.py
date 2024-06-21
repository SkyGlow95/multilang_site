# main/admin.py

from django.contrib import admin
from .models import Article

# Enregistrement du modèle Article dans l'interface d'administration Django.
# Cela permet de gérer les articles via l'interface d'administration.
admin.site.register(Article)
