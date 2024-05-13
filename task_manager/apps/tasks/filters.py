import django_filters

from task_manager.apps.tasks.models import Task


class TaskFilter(django_filters.FilterSet):

    class Meta:
        model = Task
        fields = ["status", "executor", "labels"]