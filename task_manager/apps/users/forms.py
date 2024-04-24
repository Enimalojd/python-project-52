from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
    first_name = forms.CharField(
        label='Имя',
    )
    last_name = forms.CharField(
        label='Фамилия',
    )
    password1 = forms.CharField(
        label='Пароль',
    )
    password2 = forms.CharField(
        label='Подтверждение пароля',
    )
    username = forms.CharField(
        label='Логин',
    )
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
