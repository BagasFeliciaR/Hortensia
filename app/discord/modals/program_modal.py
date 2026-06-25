import discord

from app.services.program_service import ProgramService


class ProgramModal(discord.ui.Modal, title="Tambah Program"):

    program_name = discord.ui.TextInput(
        label="Program Name",
        placeholder="DPG Media",
        required=True,
        max_length=255,
    )

    platform = discord.ui.TextInput(
        label="Platform",
        placeholder="Intigriti",
        required=True,
        max_length=100,
    )

    program_url = discord.ui.TextInput(
        label="Program URL",
        placeholder="https://...",
        required=True,
        max_length=500,
    )

    description = discord.ui.TextInput(
        label="Description",
        style=discord.TextStyle.paragraph,
        required=False,
        max_length=4000,
    )

    async def on_submit(self, interaction: discord.Interaction):

        print("=" * 60)
        print("PROGRAM MODAL")
        print(self.program_name.value)
        print(self.platform.value)
        print(self.program_url.value)
        print("=" * 60)

        service = ProgramService()

        try:

            program = service.create_program(
                name=self.program_name.value,
                platform=self.platform.value,
                program_url=self.program_url.value,
                status="ACTIVE",
            )

            print(f"Created program #{program.id}")

            await interaction.response.send_message(
                f"✅ Program #{program.id} berhasil dibuat.",
                ephemeral=True,
            )

        except Exception:
            import traceback

            traceback.print_exc()

            await interaction.response.send_message(
                "Terjadi error. Lihat terminal.",
                ephemeral=True,
            )
