from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _

from task_manager.apps.statuses.forms import StatusForm
from task_manager.apps.statuses.models import Status
from task_manager.mixins import CustomLoginRequiredMixin


class Index(CustomLoginRequiredMixin, ListView):
    model = Status
    template_name = "statuses/statuses.html"
    context_object_name = "statuses"
    login_url = "login"


class StatusCreateView(CustomLoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = StatusForm
    template_name = "statuses/create_status.html"
    success_url = reverse_lazy("statuses")
    success_message = _("Status successfully created")
    login_url = "login"


class StatusUpdateView(CustomLoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Status
    fields = ("name",)
    template_name = "statuses/update_status.html"
    success_url = reverse_lazy("statuses")
    success_message = _("Status successfully updated")
    login_url = "login"


class StatusDeleteView(CustomLoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Status
    template_name = "statuses/delete_status.html"
    success_url = reverse_lazy("statuses")
    success_message = _("Status successfully deleted")
    login_url = "login"
