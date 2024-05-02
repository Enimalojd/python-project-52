from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin

from task_manager.apps.tasks.forms import TaskForm
from task_manager.apps.tasks.models import Task


class Index(LoginRequiredMixin, ListView):
    model = Task
    template_name = "tasks/tasks.html"
    context_object_name = "tasks"
    login_url = "login"


class TaskCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = TaskForm
    template_name = "tasks/create_task.html"
    success_url = reverse_lazy("tasks")
    success_message = "Задача успешно создана"
    login_url = "login"


class TaskUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Task
    fields = ("name",)
    template_name = "tasks/update_task.html"
    success_url = reverse_lazy("tasks")
    success_message = "Задача успешно изменена"
    login_url = "login"


class TaskDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Task
    template_name = "tasks/delete_task.html"
    success_url = reverse_lazy("tasks")
    success_message = "Задача успешно удалена"
    login_url = "login"


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = "tasks/current_task.html"
    login_url = "login"
    context_object_name = "task"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["labels"] = self.Label.object.filter(task=self.object)
        return context
