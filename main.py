import asyncio
import nextcord
import openpyxl
import toml
from nextcord.ext import commands


class ChessTournamentBot(commands.Bot):

    def __init__(self):
        super().__init__(command_prefix='', help_command=None, intents=nextcord.Intents.all())


def main():
    bot = ChessTournamentBot()
    bot.run(toml.load("config/config.toml")["TOKEN"])


if __name__ == "__main__":
    main()
