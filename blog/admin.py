from django.contrib import admin
from .models import Article, Category, Comment


class FilterByTitle(admin.SimpleListFilter):
    title = 'تکرار مقدمه'
    parameter_name = 'title'

    def lookups(self, request, model_admin):
        return (
            ('django', 'جنگو'),
            ('python', 'پایتون'),
        )

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(title__icontains=self.value())


@admin.register(Article)
class HomeAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')
    list_filter = ('created', FilterByTitle)
    search_fields = ('title', 'description')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('username', 'article', 'parent', 'massage', 'created')
