from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView
from django.contrib.auth.models import User
from task_manager.apps.users.forms import UserForm
from django.contrib.messages.views import SuccessMessageMixin


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
    success_message = "Пользователь успешно создан"


class UserUpdateView(SuccessMessageMixin, UpdateView):
    model = User
    fields = ("first_name", "last_name", "username")
    template_name = "users/update_user.html"
    success_message = "Пользователь успешно обновлен"
    success_url = reverse_lazy("users")


class UserDeleteView(SuccessMessageMixin, DeleteView):
    model = User
    template_name = "users/delete_user.html"
    success_url = reverse_lazy("index")
    success_message = "Пользователь успешно удален"
