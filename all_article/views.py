from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404,redirect
from django.views import generic

from blog.models import Article, Category


def all_article(request):
    article = Article.objects.all()
    paginator = Paginator(article, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'all_article/all_article.html', {'article': page_obj})


def article_category(request, pk):
    category = get_object_or_404(Category, id=pk)
    article = category.article_set.all()
    paginator = Paginator(article, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'all_article/all_article.html', {'article': page_obj})


def search_question(request):
    q = request.GET.get('q')
    if q == '':
        article = Article.objects.all()
        page_obj = Paginator(article, 1)

    else:
        article = Article.objects.filter(title__icontains=q)
        paginator = Paginator(article, 1)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    return render(request, 'all_article/all_article.html', {'article': page_obj})
