from django import forms
from django.utils.translation import gettext_lazy as _

from task_manager.apps.statuses.models import Status


class StatusForm(forms.ModelForm):
    name = forms.CharField(required=True, max_length=255, label=_("Name"))

    class Meta:
        model = Status
        fields = ("name",)
