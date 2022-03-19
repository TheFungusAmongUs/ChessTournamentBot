import nextcord
from stats import Stats
from dataclasses import dataclass


@dataclass()
class Participant:

    channel: nextcord.TextChannel
    stats: Stats
    school: str
