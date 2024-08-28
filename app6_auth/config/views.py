from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.forms import UserCreationForm


class SignUpView(CreateView):
    form_class = UserCreationForm
    # from view we provide the link via `reverse_lazy`
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'