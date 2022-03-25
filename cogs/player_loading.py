import nextcord
from asyncio import sleep
from models.participants import Participant
from models.schools import School
from models.stats import Stats
from nextcord import CategoryChannel, Guild, Interaction, slash_command
from nextcord.ext import application_checks, commands
from pandas import DataFrame, read_excel
from pickle import dump
from typing import Optional
from utils.file_handling import *

with open("config/config.toml") as config_file:
    GUILD_ID = read_toml(config_file)["GUILD_ID"]

MATCHUPS = (
    (("Richview", "Martingrove"), ("Saint Andrew's", "West Humber")),
    (("Richview", "Saint Andrew's"), ("West Humber", "Earl Haig")),
    (("Richview", "West Humber"), ("Earl Haig", "Martingrove")),
    (("Earl Haig", "Richview"), ("Saint Andrew's", "Martingrove")),
    (("Saint Andrew's", "Earl Haig"), ("West Humber", "Martingrove"))
)

schools: dict[str, School] = {}


class PlayerLoadingCog(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.schools = ["Earl Haig", "Martingrove", "West Humber", "Saint Andrew's", "Richview"]
        self.guild: Optional[Guild] = None

    @commands.Cog.listener()
    async def on_ready(self):
        self.guild = self.bot.get_guild(GUILD_ID)

    @slash_command(
        name="load_users",
        description="loads users from a spreadsheet",
        guild_ids=[GUILD_ID]
    )
    @application_checks.is_owner()
    async def load_users(self, interaction: Interaction):
        global schools
        await self.bot.wait_until_ready()
        print("loading users...")

        with open("data/data.pkl", "r+b") as data_file:
            dump((school_list := await self._load_schools()), data_file)

        schools = dict(zip(self.schools, school_list))
        for school_name, school in schools.items():
            for hour_num, hour in enumerate(MATCHUPS):
                for pairing in hour:
                    if school_name == pairing[0]:
                        school.matchups[hour_num] = schools[pairing[1]]
                    elif school_name == pairing[1]:
                        school.matchups[hour_num] = schools[pairing[0]]

        for school in schools.values():
            for rank, part in enumerate(school.participants):
                if part.sub:
                    break
                embed = nextcord.Embed(
                    title="Opponents"
                )
                for hour, matchup in enumerate(school.matchups):
                    embed.add_field(
                        name=f"Match {hour + 1}",
                        value=f"{matchup.participants[rank].get_member(self.guild)}"
                              f" ({matchup.participants[rank].username})"
                        if matchup else "Bye"
                    )
                    if matchup:
                        part.matchups[hour] = matchup.participants[rank]

                await part.get_channel(self.bot).send(embed=embed)

    async def _load_schools(self) -> list[School]:
        school_list: list[School] = []
        for school in self.schools:
            df: DataFrame = read_excel(f"data/{school}.xlsx", engine="openpyxl", sheet_name=0)
            cat: CategoryChannel = await self.guild.create_category(
                name=school,
                overwrites={self.guild.default_role: nextcord.PermissionOverwrite(send_messages=False)}
            )

            school_list.append(School(
                await self._load_participants_for_school(cat, df, school),
                Stats(),
                school
            ))

        return school_list

    async def _load_participants_for_school(self, cat: CategoryChannel, df: DataFrame, school: str) -> list[
        Participant]:
        part_list: list[Participant] = []
        for num, participant in enumerate(map(lambda row: row[1], df.iterrows())):
            print(participant)
            part_obj = Participant(
                int(participant["Discord ID"][1:]),
                participant["Name"],
                school,
                Stats(),
                (num > 6),
                participant["Chess.com Username"]
            )
            if not part_obj.sub:
                await sleep(0.69)
                ch: nextcord.TextChannel = await self.guild.create_text_channel(name=participant["Name"], category=cat)
                part_obj.channel = ch.id
            part_list.append(part_obj)
        return part_list
