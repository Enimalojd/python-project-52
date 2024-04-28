from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from task_manager.apps.statuses.forms import StatusForm
from task_manager.apps.statuses.models import Status
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin


class Index(LoginRequiredMixin, ListView):
    model = Status
    template_name = "statuses/statuses.html"
    context_object_name = "statuses"
    login_url = "login"


class StatusCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = StatusForm
    template_name = "statuses/create_status.html"
    success_url = reverse_lazy("statuses")
    success_message = "Статус успешно создан"
    login_url = "login"


class StatusUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Status
    fields = ("name",)
    template_name = "statuses/update_status.html"
    success_url = reverse_lazy("statuses")
    success_message = "Статус успешно изменён"
    login_url = "login"


class StatusDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Status
    template_name = "statuses/delete_status.html"
    success_url = reverse_lazy("statuses")
    success_message = "Статус успешно удален"
    login_url = "login"
