import re

from discord.ext import commands


class Market(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.post = False

    @commands.command(name="sell")
    async def sell(self, ctx, item: str, quantity: str, price: str):
        await self.bot.sub_send("market", "post for_coins", type="sell", quantity=quantity,
                                item=item, for_coins=f"{quantity}*{price}", days="5", allow_partial=True)
        self.post = True
        await ctx.reply("Done")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id != self.bot.channel_id or not self.bot.config["state"] or not self.post:
            return

        for embed in message.embeds:
            embed = embed.to_dict()
            try:
                if "Are you sure that you want to post this offer?" in embed["description"]:
                    await self.bot.click(message, 0, 1)
                    self.post = False
            except KeyError:
                pass


async def setup(bot):
    await bot.add_cog(Market(bot))
