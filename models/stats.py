from dataclasses import dataclass


@dataclass()
class Stats:

    wins: int
    draws: int
    losses: int

    def total_points(self) -> float:
        return self.wins + self.draws * 0.5
