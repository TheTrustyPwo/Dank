import asyncio
import random

from discord.ext import commands


class Pm(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id != self.bot.channel_id or not self.bot.config["state"]:
            return

        for embed in message.embeds:
            embed = embed.to_dict()
            try:
                if "Meme Posting Session" in embed["author"]["name"]:
                    self.bot.lock = True
                    await self.bot.select(message, 0, 0, random.randint(0, 3))
                    await asyncio.sleep(0.2)
                    await self.bot.select(message, 1, 0, random.randint(0, 4))
                    await asyncio.sleep(0.2)
                    await self.bot.click(message, 2, 0)
                    self.bot.lock = False
            except KeyError:
                pass


async def setup(bot):
    await bot.add_cog(Pm(bot))
