from abc import ABC, abstractmethod
from typing import Iterable

from task_manager.apps.statuses.entities import Status
from task_manager.apps.statuses.models import Status as StatusModel


class BaseStatusService(ABC):

    @abstractmethod
    def get_status_list(self) -> Iterable[Status]: ...

    @abstractmethod
    def get_status_count(self) -> int: ...


class ORMStatusService(BaseStatusService):

    def get_status_list(self) -> Iterable[Status]:
        qs = StatusModel.objects.filter()

        return [status.to_entity() for status in qs]

    def get_status_count(self) -> int:
        return StatusModel.objects.filter().count()
