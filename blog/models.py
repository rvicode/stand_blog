from django.db import models
from accounts.models import CustomUser


class Category(models.Model):
    title = models.CharField(max_length=40)

    def __str__(self):
        return str(self.title or '')


class Article(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    topic = models.ManyToManyField(Category, related_query_name='topic_list')
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    slug = models.SlugField(default=title)
    image = models.ImageField(upload_to='media/blog/article')

    def __str__(self):
        return str(self.title or '')


class Comment(models.Model):
    username = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='comment')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comment')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='reply', null=True, blank=True)
    massage = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.massage)
