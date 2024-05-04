from django.db import models
from django.utils.translation import gettext_lazy as _

from task_manager.apps.labels.models import Label
from task_manager.apps.statuses.models import Status
from task_manager.apps.users.models import User


class Task(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, unique=True)
    description = models.TextField(null=True, blank=True)
    status = models.ForeignKey(
        Status, on_delete=models.PROTECT, null=False, blank=False
    )
    executor = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="executor",
    )
    labels = models.ManyToManyField(Label, blank=True)
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        null=False,
        blank=False,
        related_name="author",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
