from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView
from task_manager.apps.labels.forms import LabelForm
from task_manager.apps.labels.models import Label
from django.contrib.messages.views import SuccessMessageMixin


class Index(ListView):
    model = Label
    template_name = "labels/labels.html"
    context_object_name = "labels"
    login_url = "login"


class LabelCreateView(SuccessMessageMixin, CreateView):
    form_class = LabelForm
    template_name = "labels/create_label.html"
    success_url = reverse_lazy("labels")
    success_message = "Метка успешно создана"
    login_url = "login"


class LabelUpdateView(SuccessMessageMixin, UpdateView):
    model = Label
    fields = ("name",)
    template_name = "labels/update_label.html"
    success_message = "Метка успешно обновлена"
    success_url = reverse_lazy("labels")
    login_url = "login"


class LabelDeleteView(SuccessMessageMixin, DeleteView):
    model = Label
    template_name = "labels/delete_label.html"
    success_url = reverse_lazy("labels")
    success_message = "Метка успешно удалена"
    login_url = "login"
