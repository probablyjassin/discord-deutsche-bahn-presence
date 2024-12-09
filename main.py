import os
import discord
from discord.ext import commands

from config import DISCORD_TOKEN

""" with Presence(CLIENT_ID) as presence:
    print("Connected")
    presence.set(
        {
            "state": "In Game",
            "details": "Mario Kart 8 Deluxe",
            "timestamps": {"start": int(time.time())},
        }
    )
    print("Presence updated")

    while True:
        time.sleep(15)
 """

intents = discord.Intents.all()


class DeutscheBahnPresenceBot(commands.Bot):
    """
    A custom Discord bot class.

    This class extends the `commands.Bot` class from the `discord.ext.commands` module.
    """

    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)

    async def close(self):
        for name, cog in self.cogs.items():
            cog._eject(self)
            print(f"Ejected {name}")
        await super().close()


bot = DeutscheBahnPresenceBot(
    command_prefix=".",
    case_insensitive=True,
    help_command=None,
    intents=intents,
    status=discord.Status.online,
    activity=discord.Streaming(
        name="ones and zeroes...", url="https://www.youtube.com/watch?v=xvFZjo5PgG0"
    ),
)


@bot.event
async def on_ready():
    print(f"Bot connected as {bot.user}")
    print("Rich Presence connected")


def main():
    print("----Loading extensions----")
    for root, dirs, files in os.walk("./cogs"):
        for file in files:
            if file.endswith(".py"):
                cog_path = os.path.join(root, file)
                extension = (
                    cog_path[2:].replace("/", ".").replace("\\", ".").replace(".py", "")
                )
                bot.load_extension(extension)
                print(f"Loaded {extension}")

    bot.run(DISCORD_TOKEN)


if __name__ == "__main__":
    main()
