from django.http.response import HttpResponse as HttpResponse
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.messages.views import SuccessMessageMixin


class IndexView(TemplateView):
    template_name = 'index.html'


class UserLogin(SuccessMessageMixin, LoginView):
    template_name = 'auth/login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('index')


class UserLogout(LogoutView):
    next_page = reverse_lazy('index')
