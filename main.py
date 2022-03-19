import asyncio
import nextcord
import pandas
import toml
from nextcord.ext import application_checks, commands


class ChessTournamentBot(commands.Bot):

    SCHOOLS: dict[str, pandas.DataFrame] = {
        "West Humber": ...,
        "Saint Andrew's": ...,
        "Earl Haig": ...,
        "Martingrove": ...,
        "Richview": ...
    }

    def __init__(self):
        super().__init__(command_prefix='', help_command=None, intents=nextcord.Intents.all())

    def on_ready(self):
        print(nextcord.__version__)

    @nextcord.slash_command(
        name="load_users",
        description="loads users from a spreadsheet",
        guild_ids=[951146346335862844]
    )
    @application_checks.is_owner()
    async def load_users(self, interaction: nextcord.Interaction):
        for school, df in self.SCHOOLS.items():
            df = pandas.read_excel(f"data/{school}.xlsx", engine="openpyxl")


def main():
    bot = ChessTournamentBot()
    bot.run(toml.load("config/config.toml")["TOKEN"])


if __name__ == "__main__":
    main()
