import re

from discord.ext import commands


class Hl(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id != self.bot.channel_id or not self.bot.config_dict[self.bot.account_id]["state"] or not \
                self.bot.config_dict[self.bot.account_id]["commands"]["hl"]:
            return

        for embed in message.embeds:
            embed = embed.to_dict()
            try:
                if "I just chose a secret number" in embed["description"]:
                    num = int(re.search("\*\*(.*?)\*\*", embed["description"]).group(1).title())
                    if num >= 50:
                        await self.bot.click(message, 0, 0)
                    else:
                        await self.bot.click(message, 0, 2)
            except KeyError:
                pass


async def setup(bot):
    await bot.add_cog(Hl(bot))
