from abc import ABC, abstractmethod
from typing import Iterable

from task_manager.apps.labels.entities import Label
from task_manager.apps.labels.models import Label as LabelModel


class BaseLabelService(ABC):
    @abstractmethod
    def get_label_list(self) -> Iterable[Label]: ...

    @abstractmethod
    def get_label_count(self) -> int: ...


class ORMLabelService(BaseLabelService):

    def get_label_list(self) -> Iterable[Label]:
        qs = LabelModel.objects.filter()

        return [label.to_entity() for label in qs]

    def get_label_count(self) -> int:
        return LabelModel.objects.filter().count()
