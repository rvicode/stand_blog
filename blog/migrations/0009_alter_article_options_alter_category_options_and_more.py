# Generated by Django 4.0.6 on 2022-07-30 08:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0008_alter_article_topic'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'مقاله', 'verbose_name_plural': 'مقاله ها'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'دسته بندی', 'verbose_name_plural': 'دسته بندی ها'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'کامنت', 'verbose_name_plural': 'کامنت ها'},
        ),
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='نویسنده'),
        ),
        migrations.AlterField(
            model_name='article',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='تاریخ نشر'),
        ),
        migrations.AlterField(
            model_name='article',
            name='description',
            field=models.TextField(verbose_name='بدنه'),
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(upload_to='media/blog/article', verbose_name='تصویر'),
        ),
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(default=models.CharField(max_length=40, verbose_name='مقدمه')),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=40, verbose_name='مقدمه'),
        ),
        migrations.AlterField(
            model_name='article',
            name='topic',
            field=models.ManyToManyField(related_query_name='topic_list', to='blog.category', verbose_name='موضوع'),
        ),
        migrations.AlterField(
            model_name='article',
            name='update',
            field=models.DateTimeField(auto_now=True, verbose_name='تاریخ بروز رسانی'),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=40, verbose_name='مقدمه'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='blog.article', verbose_name='مقاله'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='تاریخ'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='massage',
            field=models.TextField(verbose_name='پیام'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reply', to='blog.comment', verbose_name='پاسخ به کامنت'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to=settings.AUTH_USER_MODEL, verbose_name='نام کاربری'),
        ),
    ]