from django.urls import path
from . import views


urlpatterns = [
    path('article/', views.all_article, name='all_article'),
    path('category/<int:pk>', views.article_category, name='article_category'),
    path('search', views.search_question, name='search_question'),
]
