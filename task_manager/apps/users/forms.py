from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _

from task_manager.apps.users.models import User


class UserForm(UserCreationForm):
    first_name = forms.CharField(required=True, label=_("First name"))
    last_name = forms.CharField(required=True, label=_("Last name"))
    username = forms.CharField(
        required=True,
        label=_("Username"),
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
    )
    password1 = forms.CharField(
        required=True,
        label=_("password1"),
        help_text=_("Your password must contain at least 3 characters."),
    )
    password2 = forms.CharField(
        required=True,
        label=_("password2"),
        help_text=_("To confirm, please enter your password again."),
    )

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "password1",
            "password2",
        )
