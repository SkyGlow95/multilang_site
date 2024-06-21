from django import forms
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import Article

class ArticleForm(forms.ModelForm):
    text = forms.CharField(
        label=_('Text'),  # Traduction du label
        widget=CKEditorUploadingWidget(config_name='default')
    )
    title = forms.CharField(
        label=_('Title'),  # Traduction du label
    )

    class Meta:
        model = Article
        fields = ['title', 'text']
