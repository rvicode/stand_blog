from django.urls import path
from . import views


urlpatterns = [
    path('singup', views.SingUpView.as_view(), name='singup'),
]
