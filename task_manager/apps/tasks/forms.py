from django import forms
from django.utils.translation import gettext_lazy as _

from task_manager.apps.tasks.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = (
            _("name"),
            _("description"),
            _("status"),
            _("executor"),
            _("labels"),
        )
