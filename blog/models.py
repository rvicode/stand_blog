from django.db import models
from django.utils.html import format_html

from accounts.models import CustomUser


class Category(models.Model):
    title = models.CharField(max_length=40, verbose_name='مقدمه')

    def __str__(self):
        return str(self.title or '')

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


class Article(models.Model):
    title = models.CharField(max_length=40, verbose_name='مقدمه')
    description = models.TextField(verbose_name='بدنه')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='نویسنده')
    topic = models.ManyToManyField(Category, related_query_name='topic_list', verbose_name='موضوع')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ نشر')
    update = models.DateTimeField(auto_now=True, verbose_name='تاریخ بروز رسانی')
    slug = models.SlugField(default=title)
    image = models.ImageField(upload_to='media/blog/article', verbose_name='تصویر', blank=True, null=True)

    def __str__(self):
        return str(self.title or '')

    def show_image(self):
        if self.image:
            return format_html(f'<img src="{self.image.url}" height="50px" width="60px">')
        return format_html('<h3 style="color:red;"> تصویری وجود ندارد</h3>')
    show_image.short_description = 'تصویر'

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقاله ها'


class Comment(models.Model):
    username = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='comment',
                                 verbose_name='نام کاربری')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comment', verbose_name='مقاله')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='reply', null=True, blank=True,
                               verbose_name='پاسخ به کامنت')
    massage = models.TextField(verbose_name='پیام')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ')

    def __str__(self):
        return str(self.massage)

    class Meta:
        verbose_name = 'کامنت'
        verbose_name_plural = 'کامنت ها'
