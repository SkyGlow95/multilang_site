from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import Article

class ArticleForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget(config_name='default'))

    class Meta:
        model = Article
        fields = ['title', 'text']
