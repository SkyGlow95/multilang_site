from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Article(models.Model):
    title = models.CharField('Title', max_length=200)
    text = RichTextUploadingField('Text', config_name='extends', default='')
    published_date = models.DateTimeField('Published Date', auto_now_add=True)

    def __str__(self):
        return self.title
