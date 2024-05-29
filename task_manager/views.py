from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _
from django.contrib import messages

from task_manager.mixins import MessageMixin


class IndexView(TemplateView):
    template_name = "index.html"


class UserLoginView(SuccessMessageMixin, LoginView):
    template_name = "auth/login.html"
    form_class = AuthenticationForm
    success_url = reverse_lazy("index")
    success_message = _("You are logged in")


class UserLogoutView(MessageMixin, LogoutView):
    next_page = reverse_lazy("index")
    info_message = _("You are logged out")
