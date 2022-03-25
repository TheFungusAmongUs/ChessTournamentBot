from dataclasses import dataclass


@dataclass()
class Stats:

    wins: int = 0
    draws: int = 0
    losses: int = 0

    def total_points(self) -> float:
        return self.wins + self.draws * 0.5
