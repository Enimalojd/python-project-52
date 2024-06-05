from abc import ABC, abstractmethod
from typing import Iterable

from task_manager.apps.tasks.entities import Task
from task_manager.apps.tasks.models import Task as TaskModel


class BaseTaskService(ABC):

    @abstractmethod
    def get_task_list(self) -> Iterable[Task]: ...

    @abstractmethod
    def get_task_count(self) -> int: ...


class ORMTaskService(BaseTaskService):

    def get_task_list(self) -> Iterable[Task]:
        qs = TaskModel.objects.filter()

        return [task.to_entity() for task in qs]

    def get_task_count(self) -> int:
        return TaskModel.objects.filter().count()
