from django.db import models
from django.utils.translation import gettext_lazy as _


class Task(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, unique=True)
    description = models.TextField(null=True, blank=True)
    status = models.ForeignKey(
        "statuses.Status", on_delete=models.PROTECT, null=False, blank=False
    )
    executor = models.ForeignKey(
        "users.User", on_delete=models.PROTECT, null=True, blank=True
    )
    tag = models.ManyToManyField(
        "tags.Tag", blank=True, related_name="tasks", verbose_name=_("Тэги")
    )
    author = models.ForeignKey(
        "users.User", on_delete=models.PROTECT, null=False, blank=False
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
