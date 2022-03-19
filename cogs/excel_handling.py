import toml
from nextcord import Interaction, slash_command
from nextcord.ext import application_checks, commands
from pandas import DataFrame, read_excel


class ExcelCog(commands.Cog):

    def __init__(self, bot: commands.Bot, schools: dict[str, DataFrame]):
        self.bot = bot
        self.schools = schools

    @slash_command(
        name="load_users",
        description="loads users from a spreadsheet",
        guild_ids=[toml.load("config/config.toml")["GUILD_ID"]]
    )
    @application_checks.is_owner()
    async def load_users(self, interaction: Interaction):
        print("loading users...")
        for school, df in self.schools.items():
            df = read_excel(f"data/{school}.xlsx", engine="openpyxl", sheet_name=0)




