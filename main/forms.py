# Importation des modules nécessaires
from django import forms
from django.utils.translation import gettext_lazy as _  # Importation pour les traductions
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import Article

# Définition du formulaire pour le modèle Article
class ArticleForm(forms.ModelForm):
    # Champ pour le texte de l'article avec CKEditor
    text = forms.CharField(
        label=_('Text'),  # Traduction du label
        widget=CKEditorUploadingWidget(config_name='default')  # Utilisation de CKEditor pour ce champ
    )
    
    # Champ pour le titre de l'article
    title = forms.CharField(
        label=_('Title'),  # Traduction du label
    )

    # Meta informations pour le formulaire
    class Meta:
        model = Article  # Modèle lié à ce formulaire
        fields = ['title', 'text']  # Champs du modèle inclus dans ce formulaire
