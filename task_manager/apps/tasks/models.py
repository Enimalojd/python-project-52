from django.db import models
from django.utils.translation import gettext_lazy as _

from task_manager.apps.labels.models import Label
from task_manager.apps.statuses.models import Status
from task_manager.apps.users.models import User


class Task(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name=_("Name"))
    description = models.TextField(max_length=300, verbose_name=_("Description"))
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        related_name="statuses",
        verbose_name=_("Status"),
    )
    executor = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="executor",
        verbose_name=_("Executor"),
    )
    labels = models.ManyToManyField(
        Label,
        blank=True,
        related_name="labels",
        verbose_name=_("Labels"),
        through="TaskLabel",
        through_fields=("task", "label"),
    )
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="author",
        verbose_name=_("Author"),
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created at"))

    def __str__(self):
        return self.name


class TaskLabel(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    label = models.ForeignKey(Label, on_delete=models.PROTECT)
