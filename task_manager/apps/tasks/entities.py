from dataclasses import dataclass
from datetime import datetime
from typing import List

from task_manager.apps.labels.entities import Label


@dataclass
class Task:
    id: int
    name: str
    description: str
    status: str
    author: str
    executor: str
    labels: List[Label]
    created_at: datetime
