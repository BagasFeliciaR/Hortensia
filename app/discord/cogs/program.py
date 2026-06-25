from discord.ext import commands
from discord import app_commands

from app.discord.modals.program_modal import ProgramModal


class ProgramCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="program",
        description="Tambah Program"
    )
    async def program(
        self,
        interaction,
    ):

        await interaction.response.send_modal(
            ProgramModal()
        )


async def setup(bot):
    await bot.add_cog(
        ProgramCog(bot)
    )
