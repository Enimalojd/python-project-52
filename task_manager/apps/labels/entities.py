from dataclasses import dataclass
from datetime import datetime


@dataclass
class Label:
    id: int
    name: str
    created_at: datetime
