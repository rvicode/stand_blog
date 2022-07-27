from django.shortcuts import render, get_object_or_404, redirect

from blog.models import Article, Comment


def article_detail(request, pk):
    article = get_object_or_404(Article, slug=pk)
    if request.method == 'POST':
        massage = request.POST.get('message')
        parent_id = request.POST.get('parent_id')
        Comment.objects.create(article=article, username=request.user, massage=massage, parent_id=parent_id)
    return render(request, 'article_details/article_details.html', {'article': article})
