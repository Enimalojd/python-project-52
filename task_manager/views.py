from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic import FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm


class IndexView(TemplateView):
    template_name = 'index.html'


class Login(LoginView):
    template_name = 'auth/login.html'
    form_class = AuthenticationForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class Logout(FormView):
    template_name = 'auth/logout.html'
    success_url = reverse_lazy('index')
