from abc import ABC, abstractmethod
from typing import Iterable

from task_manager.apps.users.entities import User
from task_manager.apps.users.models import User as UserModel


class BaseUserService(ABC):

    @abstractmethod
    def get_user_list(self) -> Iterable[User]:
        raise NotImplementedError()

    @abstractmethod
    def get_user_count(self) -> int:
        raise NotImplementedError()


class ORMUserService(BaseUserService):

    def get_user_list(self) -> Iterable[User]:
        qs = UserModel.objects.filter()

        return [user.to_entity() for user in qs]

    def get_user_count(self) -> int:
        return UserModel.objects.filter().count()
