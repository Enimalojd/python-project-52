from ninja import Router

from task_manager.api.v1.tasks.schemas import TaskListSchema, TaskSchema
from task_manager.apps.tasks.services.tasks import BaseTaskService, ORMTaskService


router = Router(tags=["Tasks"])


@router.get("/", response=TaskListSchema)
def get_task_list_handler(requst) -> TaskListSchema:
    service: BaseTaskService = ORMTaskService()
    list_task = service.get_task_list()

    return [TaskSchema.from_entity(obj) for obj in list_task]
