from django import forms
from django.utils.translation import gettext_lazy as _

from task_manager.apps.labels.models import Label
from task_manager.apps.statuses.models import Status
from task_manager.apps.tasks.models import Task
from task_manager.apps.users.models import User


class TaskForm(forms.ModelForm):
    name = forms.CharField(required=True, max_length=255)
    description = forms.CharField(widget=forms.Textarea)
    status = forms.ModelChoiceField(queryset=Status.objects.all())
    executor = forms.ModelChoiceField(queryset=User.objects.all())
    labels = forms.ModelMultipleChoiceField(
        queryset=Label.objects.all(),
        required=False,
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
