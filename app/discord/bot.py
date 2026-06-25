import discord

from discord.ext import commands

from app.config.settings import settings

intents = discord.Intents.default()

bot = commands.Bot(
    command_prefix="!",
    intents=intents,
)


@bot.event
async def on_ready():

    print(f"Logged in as {bot.user}")

    try:

        await bot.load_extension(
            "app.discord.cogs.program"
        )

    except commands.ExtensionAlreadyLoaded:
        pass

    synced = await bot.tree.sync()

    print(f"Synced {len(synced)} commands")


def run():
    bot.run(settings.DISCORD_TOKEN)
