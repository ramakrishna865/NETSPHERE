from django.shortcuts import render, get_object_or_404
from .models import NewsArticle

def article_list(request):
    articles = NewsArticle.objects.all()
    return render(request, 'App_News/article_list.html', {'articles': articles})

def article_detail(request, pk):
    article = get_object_or_404(NewsArticle, pk=pk)
    return render(request, 'App_News/article_details.html', {'article': article})
