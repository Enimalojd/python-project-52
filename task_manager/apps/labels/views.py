from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _

from task_manager.apps.labels.forms import LabelForm
from task_manager.apps.labels.models import Label
from task_manager.mixins import CustomLoginRequiredMixin, DeleteMixin


class Index(CustomLoginRequiredMixin, ListView):
    model = Label
    template_name = "labels/labels.html"
    context_object_name = "labels"
    login_url = "login"


class LabelCreateView(CustomLoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = LabelForm
    template_name = "labels/create_label.html"
    success_url = reverse_lazy("labels")
    success_message = _("Label successfully created")
    login_url = "login"


class LabelUpdateView(CustomLoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Label
    fields = ("name",)
    template_name = "labels/update_label.html"
    success_message = _("Label successfully updated")
    success_url = reverse_lazy("labels")
    login_url = "login"


class LabelDeleteView(CustomLoginRequiredMixin, SuccessMessageMixin, DeleteMixin):
    model = Label
    template_name = "labels/delete_label.html"
    success_url = reverse_lazy("labels")
    success_message = _("Label successfully deleted")
    login_url = "login"
    error_message = _("It is not possible to delete the label because it is being used")
    error_url = reverse_lazy("labels")
