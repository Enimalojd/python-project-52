from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _

from task_manager.mixins import DeleteMixin
from task_manager.apps.users.models import User
from task_manager.apps.users.forms import UserForm


class Index(ListView):
    model = User
    template_name = "users/users.html"
    context_object_name = "users"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_user"] = self.request.user
        return context


class UserCreateView(SuccessMessageMixin, CreateView):
    form_class = UserForm
    template_name = "users/create_user.html"
    success_url = reverse_lazy("login")
    success_message = _("User successfully created")


class UserUpdateView(SuccessMessageMixin, UpdateView):
    model = User
    form_class = UserForm
    template_name = "users/update_user.html"
    success_message = _("User successfully updated")
    success_url = reverse_lazy("users")


class UserDeleteView(SuccessMessageMixin, DeleteMixin):
    model = User
    template_name = "users/delete_user.html"
    success_url = reverse_lazy("users")
    success_message = _("User successfully deleted")
    error_message = _("Cannot delete user because it is in use")
    error_url = reverse_lazy("users")
