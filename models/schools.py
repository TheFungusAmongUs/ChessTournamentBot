from dataclasses import dataclass, field
from models.participants import Participant
from models.stats import Stats
from typing import Optional


@dataclass()
class School:

    participants: list[Participant]
    stats: Stats
    name: str
    matchups: Optional[list['School']] = field(default_factory=lambda: [None, None, None, None, None])
