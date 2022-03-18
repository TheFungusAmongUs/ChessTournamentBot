import asyncio
import toml
from discord.ext import commands


class GTAHSBot(commands.Bot):

    def __init__(self):
        super().__init__(command_prefix='', help_command=None)


async def main():
    bot = GTAHSBot()
    async with bot:
        await bot.start(toml.load("config/config.toml")["TOKEN"])


if __name__ == "__main__":
    asyncio.run(main())
