import nextcord
import pandas
import toml
from nextcord.ext import commands
from cogs.excel_handling import ExcelCog

SCHOOLS: dict[str, pandas.DataFrame] = {
        "West Humber": ...,
        "Saint Andrew's": ...,
        "Earl Haig": ...,
        "Martingrove": ...,
        "Richview": ...
    }


class ChessTournamentBot(commands.Bot):

    def __init__(self):
        super().__init__(command_prefix='', help_command=None, intents=nextcord.Intents.all())

    async def on_ready(self):
        print(nextcord.__version__)


def main():
    bot = ChessTournamentBot()
    bot.add_cog(ExcelCog(bot, SCHOOLS))
    bot.run(toml.load("config/config.toml")["TOKEN"])


if __name__ == "__main__":
    main()
