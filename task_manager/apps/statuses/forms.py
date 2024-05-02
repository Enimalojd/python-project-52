from django import forms

from task_manager.apps.statuses.models import Status


class StatusForm(forms.ModelForm):
    name = forms.CharField(required=True, max_length=255)

    class Meta:
        model = Status
        fields = ("name",)
