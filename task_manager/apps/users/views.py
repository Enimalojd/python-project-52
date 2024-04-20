from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic.base import TemplateView


class Index(TemplateView):
    template_name = 'index.html'


class Login(LoginView):
    template_name = 'auth/login.html'
    next_page = '/'


class Logout(LoginView):
    template_name = 'auth/logout.html'
    next_page = '/'
    
