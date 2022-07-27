from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserCreateForm


class SingUpView(generic.CreateView):
    form_class = CustomUserCreateForm
    template_name = 'registration/singup.html'
    success_url = reverse_lazy('login')
