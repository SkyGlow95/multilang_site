# main/views.py

from .models import Article
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm
from openai import OpenAI, RateLimitError, OpenAIError
from django.conf import settings
from django.utils.translation import get_language
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

def home(request):
    return render(request, 'main/home.html')

def article_list(request):
    articles = Article.objects.all().order_by('-published_date')
    return render(request, 'main/article_list.html', {'articles': articles})

@login_required
def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('article_list')
    else:
        form = ArticleForm()
    return render(request, 'main/add_article.html', {'form': form})

@login_required
def delete_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == "POST":
        article.delete()
        return redirect('article_list')
    return render(request, 'main/article_list.html', {'article': article})

@login_required
def edit_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article_list')
    else:
        form = ArticleForm(instance=article)
    return render(request, 'main/edit_article.html', {'form': form, 'article': article})


client = OpenAI(
    api_key=settings.OPENAI_API_KEY,
)

@csrf_exempt
def chatbot(request):
    answer = None
    question = None
    language = get_language()  # Obtenir la langue actuelle

    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            question = data.get('question')
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": f"You are a helpful assistant who responds in {'French' if language == 'fr' else 'English'}."},
                    {"role": "user", "content": question}
                ]
            )
            answer = response.choices[0].message.content.strip()
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except RateLimitError:
            answer = "You have exceeded your quota for the OpenAI API. Please check your plan and billing details."
            if language == 'fr':
                answer = "Vous avez dépassé votre quota pour l'API OpenAI. Veuillez vérifier votre plan et vos détails de facturation."
        except OpenAIError as e:
            answer = f"An error occurred: {e}"
            if language == 'fr':
                answer = f"Une erreur est survenue : {e}"
        except Exception as e:
            return JsonResponse({'error': f"An unexpected error occurred: {e}"}, status=500)
        return JsonResponse({'answer': answer})

    return JsonResponse({'error': 'Invalid request'}, status=400)

def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    response_text = ""
    question = ""
    error_message = ""
    language = get_language()  # Obtenir la langue actuelle

    if request.method == 'POST':
        question = request.POST.get('question')
        context_text = article.text
        content_title = article.title
        content_date = article.published_date

        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are a helpful assistant who provides information based only on the given content from an article "
                            "and responds in French if the user's language is French, otherwise in English. "
                            "Do not use any external information."
                        )
                    },
                    {
                        "role": "user",
                        "content": (
                            f"Article title: {content_title}\n"
                            f"Article published date: {content_date}\n"
                            f"Article content: {context_text}\n"
                            f"Based on this content, title, and published date only, please answer the following question: {question}\n"
                            "If the answer is not in the content, say 'The information is not present in the article.'"
                        )
                    }
                ],
                max_tokens=150
            )
            response_text = response.choices[0].message.content.strip()

            if not response_text or "The information is not present in the article." in response_text:
                response_text = "Based on the available article, I cannot provide a satisfactory answer to your question."
                if language == 'fr':
                    response_text = "D'après l'article disponible, je ne peux pas fournir une réponse satisfaisante à votre question."
        except RateLimitError:
            response_text = "You have exceeded your quota for the OpenAI API. Please check your plan and billing details."
            if language == 'fr':
                response_text = "Vous avez dépassé votre quota pour l'API OpenAI. Veuillez vérifier votre plan et vos détails de facturation."
        except OpenAIError as e:
            error_message = f"An error occurred: {e}"
            if language == 'fr':
                error_message = f"Une erreur est survenue : {e}"

    return render(request, 'main/article_detail.html', {'article': article, 'question': question, 'response_text': response_text, 'error_message': error_message})