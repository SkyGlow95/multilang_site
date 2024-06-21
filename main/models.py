# Importation des modules nécessaires
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Définition du modèle Article
class Article(models.Model):
    # Champ pour le titre de l'article
    title = models.CharField('Title', max_length=200)

    # Champ pour le texte de l'article avec support de téléchargement via CKEditor
    text = RichTextUploadingField('Text', config_name='extends', default='')

    # Champ pour la date de publication, auto-rempli avec la date et l'heure actuelles lors de la création
    published_date = models.DateTimeField('Published Date', auto_now_add=True)

    # Méthode pour retourner une représentation en chaîne de caractères de l'article
    def __str__(self):
        return self.title
