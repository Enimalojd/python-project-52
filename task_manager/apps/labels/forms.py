from django import forms
from django.utils.translation import gettext_lazy as _

from task_manager.apps.labels.models import Label


class LabelForm(forms.ModelForm):
    name = forms.CharField(required=True, max_length=255)

    class Meta:
        model = Label
        fields = (_("name"),)
