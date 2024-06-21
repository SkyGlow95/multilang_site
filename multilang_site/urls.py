# main/urls.py
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static

# URL patterns pour les chemins généraux
urlpatterns = [
    # URL pour accéder à l'administration de Django
    path('admin/', admin.site.urls),
    # URL pour intégrer les routes de l'éditeur CKEditor
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

# URL patterns avec prise en charge de l'internationalisation (i18n)
urlpatterns += i18n_patterns(
    # URL pour les vues principales de l'application
    path('', include('main.urls')),
    # URL pour les chemins de changement de langue
    path('i18n/', include('django.conf.urls.i18n')),
)

# Ajout des URLs pour servir les fichiers médias et statiques en mode DEBUG
if settings.DEBUG:
    # URL pour servir les fichiers médias
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # URL pour servir les fichiers statiques
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
