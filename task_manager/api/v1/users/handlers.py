from ninja import Router

from task_manager.api.v1.users.schemas import UserListSchema, UserSchema
from task_manager.apps.users.services.users import BaseUserService, ORMUserService


router = Router(tags=["Users"])


@router.get("", response=UserListSchema)
def get_user_list_handler(requset) -> UserListSchema:
    service: BaseUserService = ORMUserService()
    user_list = service.get_user_list()

    return [UserSchema.from_entity(obj) for obj in user_list]
