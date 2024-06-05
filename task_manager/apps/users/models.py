from django.contrib.auth.models import AbstractUser

from task_manager.apps.users.entities import User as UserEntity


class User(AbstractUser):

    def to_entity(self):
        return UserEntity(
            id=self.id,
            first_name=self.first_name,
            last_name=self.last_name,
            username=self.username,
            date_joined=self.date_joined
        )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
