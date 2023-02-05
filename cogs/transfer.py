import re
import asyncio

from discord.ext import commands
from discord import Member


configurations = {
    "starter": [
        ("Fishing Pole", 1),
        ("Cell Phone", 1),
        ("Hunting Rifle", 1),
        ("Shovel", 1),
        ("Ammo", 8),
        ("Fishing Bait", 8),
        ("Pizza", 8),
        ("Lucky Horseshoe", 32),
        ("Cowboy Boots", 1),
        ("Daily Box", 48),
        ("Padlock", 25),
        ("Keyboard", 1),
        ("Mouse", 1),
        ("Laptop", 1),
        ("Crunchy Taco", 1),
        ("Life Saver", 100)
    ]
}


class Transfer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.transfer = False
        self.friend = None

    async def send(self, items, custom=False):
        for item in items:
            await self.bot.sub_send("friends", "share items", user=self.friend, quantity=item[1], item=item[0])
            await asyncio.sleep(3.2)

        if custom:
            self.transfer = False
            self.bot.lock = False

    @commands.command(name="transfer")
    async def sell(self, ctx, target: Member = None, conf: str = None):
        if target is None:
            await ctx.reply("You need to specify a target who is friends with you!")
            return
        self.bot.lock = True
        self.transfer = True
        self.friend = target
        if conf is None:
            await self.bot.send("inventory")
        else:
            try:
                await self.send(configurations[conf], True)
            except KeyError:
                pass

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id != self.bot.channel_id or not self.transfer or not self.friend:
            return

        for embed in message.embeds:
            embed = embed.to_dict()

            try:
                if "inventory" in embed["author"]["name"]:
                    items = []

                    for s in embed["description"].split('\n'):
                        try:
                            item = re.search("\*\*<.*> (.*)\*\* . (.*)", s).group(1)
                            amount = int(re.search("\*\*<.*> (.*)\*\* . (.*)", s).group(2).replace(',', ''))
                            if item in ["Trivia Trophy", "Birthday Cake"]:
                                continue
                            items.append((item, amount))
                        except Exception:
                            print("BAD!!!", s)

                    if not items:
                        self.transfer = False
                        self.bot.lock = False
                        return

                    await self.send(items)
                    await self.bot.send("inventory")
            except KeyError:
                pass

            try:
                if "Are you sure that you want to share" in embed["description"]:
                    await self.bot.click(message, 0, 1)
            except KeyError:
                pass


async def setup(bot):
    await bot.add_cog(Transfer(bot))
