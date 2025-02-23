from django.shortcuts import render
from django.http import HttpResponse
from .models import Article # Nuevo

def hello_world(request):
    return HttpResponse('Hola, mundo!')

def article_list(request): # Nuevo
    articles = Article.objects.all() # Nuevo
    return render(request, 'article_list.html', {'articles': articles}) # Nuevo

def article_detail(request, pk):
    article = Article.objects.get(pk=pk)
    return render(request, 'article_detail.html', {'article': article})