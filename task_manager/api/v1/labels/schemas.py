from datetime import datetime
from pydantic import BaseModel

from task_manager.apps.labels.entities import Label as LabelEntity


class LabelSchema(BaseModel):
    id: int
    name: str
    created_at: datetime

    @staticmethod
    def from_entity(entity: LabelEntity) -> "LabelSchema":
        return LabelSchema(id=entity.id, name=entity.name, created_at=entity.created_at)


LabelListSchema = list[LabelSchema]
