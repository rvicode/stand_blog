from django.contrib import admin
from .models import Article, Category, Comment


@admin.register(Article)
class HomeAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('username', 'article', 'parent', 'massage', 'created')
