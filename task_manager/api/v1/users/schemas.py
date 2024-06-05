from datetime import datetime
from pydantic import BaseModel

from task_manager.apps.users.entities import User as UserEntity


class UserSchema(BaseModel):
    id: int
    first_name: str
    last_name: str
    username: str
    date_joined: datetime

    @staticmethod
    def from_entity(entity: UserEntity) -> "UserSchema":
        return UserSchema(
            id=entity.id,
            first_name=entity.first_name,
            last_name=entity.last_name,
            username=entity.username,
            date_joined=entity.date_joined,
        )


UserListSchema = list[UserSchema]
