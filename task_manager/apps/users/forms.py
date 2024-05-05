from django import forms
from django.contrib.auth.forms import UserCreationForm

from task_manager.apps.users.models import User


class UserForm(UserCreationForm):
    first_name = forms.CharField(
        required=True,
    )
    last_name = forms.CharField(
        required=True,
    )
    username = forms.CharField(
        required=True,
    )
    password1 = forms.CharField(
        required=True,
    )
    password2 = forms.CharField(
        required=True,
    )

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "password1", "password2")
