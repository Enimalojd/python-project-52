from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _
from django_filters.views import FilterView

from task_manager.apps.tasks.forms import TaskForm
from task_manager.apps.tasks.models import Task
from task_manager.filters import TaskFilter
from task_manager.mixins import CustomLoginRequiredMixin


class Index(CustomLoginRequiredMixin, ListView, FilterView):
    model = Task
    template_name = "tasks/tasks.html"
    context_object_name = "tasks"
    login_url = "login"
    filterset_class = TaskFilter
    context_object_name = 'tasks'


class TaskCreateView(CustomLoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = TaskForm
    template_name = "tasks/create_task.html"
    success_url = reverse_lazy("tasks")
    success_message = _("Task successfully created")
    login_url = "login"


class TaskUpdateView(CustomLoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Task
    fields = ("name",)
    template_name = "tasks/update_task.html"
    success_url = reverse_lazy("tasks")
    success_message = _("Task successfully updated")
    login_url = "login"


class TaskDeleteView(CustomLoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Task
    template_name = "tasks/delete_task.html"
    success_url = reverse_lazy("tasks")
    success_message = _("Task successfully deleted")
    login_url = "login"


class TaskDetailView(CustomLoginRequiredMixin, DetailView):
    model = Task
    template_name = "tasks/current_task.html"
    login_url = "login"
    context_object_name = "task"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["labels"] = self.Label.object.filter(task=self.object)
        return context
