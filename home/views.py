from django.views import generic
from blog.models import Article


class HomeView(generic.ListView):
    template_name = 'home/home.html'
    context_object_name = 'article'

    def get_queryset(self):
        return Article.objects.all().order_by('-created')[:3]
