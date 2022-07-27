from django.urls import reverse_lazy
from django.views import generic

from .models import ContactUs
from .forms import ContactUsForm


class ContactUsView(generic.CreateView):
    model = ContactUs
    fields = ('username', 'number', 'subject', 'massage',)
    print(fields)
    template_name = 'contact_us/contact_us.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.email = self.request.user.email
        instance.save()
        return super().form_valid(form)
