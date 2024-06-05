from pydantic import BaseModel

from task_manager.apps.tasks.entities import Task as TaskEntity


class TaskSchema(BaseModel):
    id: int
    name: str
    description: str
    status: str
    author: str
    executor: str
    labels: list
    created_at: str

    @staticmethod
    def from_entity(entity: TaskEntity) -> "TaskSchema":
        return TaskSchema(
            id=entity.id,
            name=entity.name,
            description=entity.description,
            status=entity.status.name,
            author=entity.author.username,
            executor=entity.executor.username,
            labels=[label.name for label in entity.labels.all()],
            created_at=entity.created_at,
        )


TaskListSchema = list[TaskSchema]
