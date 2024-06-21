from django.urls import path
from django.contrib.auth import views as auth_views
from .views import article_list, article_detail, add_article, chatbot, home, delete_article, edit_article

# Gestion pour la navigation

urlpatterns = [
    path('', home, name='home'),
    path('chatbot/', chatbot, name='chatbot'),
    path('articles/', article_list, name='article_list'),
    path('articles/<int:article_id>/', article_detail, name='article_detail'),
    path('articles/add/', add_article, name='add_article'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('delete_article/<int:article_id>/', delete_article, name='delete_article'),
    path('edit_article/<int:article_id>/', edit_article, name='edit_article'),
]
