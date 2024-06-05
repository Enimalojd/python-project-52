from dataclasses import dataclass
from datetime import datetime


@dataclass
class Status:
    id: int
    name: str
    created_at: datetime
