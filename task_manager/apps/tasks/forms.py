from django import forms
from django.utils.translation import gettext_lazy as _

from task_manager.apps.labels.models import Label
from task_manager.apps.statuses.models import Status
from task_manager.apps.tasks.models import Task
from task_manager.apps.users.models import User


class TaskForm(forms.ModelForm):
    name = forms.CharField(required=True, max_length=255, label=_("Name"))
    description = forms.CharField(widget=forms.Textarea, label=_("Description"))
    status = forms.ModelChoiceField(queryset=Status.objects.all(), label=_("Status"))
    executor = forms.ModelChoiceField(queryset=User.objects.all(), label=_("Executor"))
    labels = forms.ModelMultipleChoiceField(
        queryset=Label.objects.all(),
        required=False,
        label=_("Labels"),
    )

    class Meta:
        model = Task
        fields = (
            "name",
            "description",
            "status",
            "executor",
            "labels",
        )
