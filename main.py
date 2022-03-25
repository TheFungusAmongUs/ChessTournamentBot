import nextcord
import os
import toml
from nextcord.ext import commands


class ChessTournamentBot(commands.Bot):

    def __init__(self):
        super().__init__(command_prefix='', help_command=None, intents=nextcord.Intents.all())

    async def on_ready(self):
        print(nextcord.__version__)


def load_extensions(bot: ChessTournamentBot):
    for file in os.listdir('./cogs'):
        if file.endswith('.py'):
            bot.load_extension(f'cogs.{file[:-3]}')


def main():
    bot = ChessTournamentBot()
    load_extensions(bot)
    bot.run(toml.load("config/config.toml")["TOKEN"])


if __name__ == "__main__":
    main()
