import django_filters
from django import forms
from django_filters import BooleanFilter, ModelChoiceFilter
from django.utils.translation import gettext_lazy as _

from task_manager.apps.labels.models import Label
from task_manager.apps.tasks.models import Task


class TaskFilter(django_filters.FilterSet):

    labels = ModelChoiceFilter(
        queryset=Label.objects.all(),
        label=_('Label')
    )

    current_user = BooleanFilter(
        field_name='author',
        label=_('Only own tasks'),
        method='show_own_tasks',
        widget=forms.CheckboxInput
    )
    class Meta:
        model = Task
        fields = ["status", "executor", "labels"]
    

    def show_own_tasks(self, queryset, name, value):
        return queryset.filter(author=self.request.user)
