from datetime import datetime
from pydantic import BaseModel

from task_manager.apps.statuses.entities import Status


class StatusSchema(BaseModel):
    name: str
    created_at: datetime

    @staticmethod
    def from_entity(entity: Status) -> "StatusSchema":
        return StatusSchema(
            id=entity.id,
            name=entity.name,
            created_at=entity.created_at,
        )
