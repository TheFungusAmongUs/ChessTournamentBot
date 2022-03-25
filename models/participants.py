import nextcord
from models.stats import Stats
from dataclasses import dataclass, field
from typing import Optional


@dataclass()
class Participant:

    member: int
    name: str
    school: str
    stats: Stats
    sub: bool
    username: str
    channel: Optional[int] = None
    matchups: Optional[list['Participant']] = field(default_factory=lambda: [None, None, None, None, None])

    def get_member(self, guild) -> nextcord.Member:
        return guild.get_member(self.member)

    def get_channel(self, bot) -> nextcord.TextChannel:
        return bot.get_channel(self.channel)
