# Generated by Django 4.0.6 on 2022-07-31 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_article_options_alter_category_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/blog/article', verbose_name='تصویر'),
        ),
    ]
