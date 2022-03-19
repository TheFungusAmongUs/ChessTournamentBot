from dataclasses import dataclass
from participants import Participant
from stats import Stats


@dataclass()
class School:

    participants: list[Participant]
    stats: Stats
    name: str
