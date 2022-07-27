from blog.models import Article, Category


def articles(request):
    article = Article.objects.all().order_by('-created')[:2]
    sidebar = Category.objects.all()
    return {'articles': article, 'sidebar': sidebar}
