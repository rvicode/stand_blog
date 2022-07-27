from django.urls import path
from . import views


urlpatterns = [
    path('detail/<slug:pk>', views.article_detail, name='article_detail'),
]