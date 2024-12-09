import discord
from discord import slash_command, Option, ApplicationContext
import time

from presence import presence_client


class presence(discord.Cog):
    def __init__(self, bot: discord.Bot) -> None:
        self.bot = bot

    @slash_command(
        name="setstatus",
        description="Set your Rich Presence details",
        integration_types={discord.IntegrationType.user_install},
    )
    async def setstatus(
        self, ctx: ApplicationContext, details=Option(str, "Enter the details")
    ):
        try:
            presence_client.set(
                {
                    "state": details,
                    "details": "frfr",
                    "timestamps": {"start": int(time.time())},
                }
            )
            await ctx.respond(f"Updated Rich Presence: {details}")
        except Exception as e:
            await ctx.respond(f"Error updating presence: {str(e)}")


def setup(bot: discord.Bot) -> None:
    bot.add_cog(presence(bot))
