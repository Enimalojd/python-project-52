from django.db import models
from django.utils.translation import gettext_lazy as _

from task_manager.apps.statuses.entities import Status as StatusEntity


class Status(models.Model):
    name = models.CharField(
        max_length=255, null=False, blank=False, verbose_name=_("Name")
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created at"))

    def to_entity(self):
        return StatusEntity(
            id=self.id,
            name=self.name,
            created_at=self.created_at,
        )

    def __str__(self) -> str:
        return self.name
