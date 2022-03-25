
import nextcord
from models.schools import School
from models.stats import Stats
from nextcord.ext import application_checks, commands
from utils.chesscom import *
from utils.file_handling import read_toml

with open("config/config.toml") as config_file:
    config_toml = read_toml(config_file)
    GUILD_ID = config_toml["GUILD_ID"]
    START_TIME = config_toml["START_TIME"]


WIN_RESULTS = ["win"]
DRAW_RESULTS = ["insufficient", "50move", "timevsinsufficient", "stalemate", "agreed", "repetition"]
LOSS_RESULTS = ["checkmated", "lose", "resigned", "timeout", "abandoned"]


class ResultsCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(
        name="record_results",
        description="Do the thing",
        guild_ids=[GUILD_ID]
    )
    @application_checks.is_owner()
    async def record_results(self, interaction: nextcord.Interaction, time_period: int):
        from cogs.player_loading import schools
        for school in schools.values():
            if not school.matchups[time_period]:
                continue
            for participant in school.participants:
                matchup = participant.matchups[time_period]
                for game in await get_player_games(participant.username):
                    if START_TIME + (time_period-1)*3600 <= game["end_time"] <= START_TIME + time_period*3600:
                        pass
