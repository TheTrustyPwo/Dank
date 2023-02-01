import asyncio
import re

from discord.ext import commands


class Autobuy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bankrob = False

    async def cog_load(self):
        await self.bot.send("use", item="Lucky Horseshoe")
        await asyncio.sleep(4)
        await self.bot.send("use", item="Pizza Slice")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.guild is None and message.author.id == 270904126974590976 and self.bot.config["state"]:
            channel = await message.author.create_dm()
            for embed in message.embeds:
                embed = embed.to_dict()

                # Buy lifesavers
                try:
                    if embed["title"] == "Your lifesaver protected you!" and \
                            self.bot.config_dict[self.bot.account_id]["autobuy"]["lifesavers"]["state"]:
                        remaining = int(
                            re.search("have (.*?)x Life Saver", message.components[0].children[0].label).group(1))
                        required = int(self.bot.config_dict[self.bot.account_id]["autobuy"]["lifesavers"]["amount"])
                        if remaining < required:
                            await self.bot.send("withdraw", channel, amount=str((required - remaining) * 100000))
                            await self.bot.sub_send("shop", "buy", channel, item="Life Saver",
                                                    quantity=str(required - remaining))
                            return
                except KeyError:
                    pass

                try:
                    if "Lucky Horseshoe expired!" in embed["description"]:
                        await self.bot.send("use", item="Lucky Horseshoe")
                    elif "Pizza Slice expired!" in embed["description"]:
                        await self.bot.send("use", item="Pizza Slice")
                    elif "Ammo expired!" in embed["description"]:
                        await self.bot.send("use", item="Ammo")
                    elif "Fishing Bait expired!" in embed["description"]:
                        await self.bot.send("use", item="Fishing Bait")
                    elif "Cowboy Boots expired!" in embed["description"]:
                        await self.bot.send("use", item="Cowboy Boots")
                    elif "your padlock broke" in embed["description"] or "stopped by your padlock" in embed[
                        "description"]:
                        await self.bot.send("use", item="Padlock")
                    elif "your bank is being robbed!" in embed["description"]:
                        self.bankrob = True
                        await self.bot.send("use", item="Cell Phone")
                except KeyError:
                    pass

                return

        if message.channel.id != self.bot.channel_id or not self.bot.config_dict[self.bot.account_id]["state"]:
            return

        for embed in message.embeds:
            embed = embed.to_dict()

            # Tools
            try:
                if "You don't have a shovel, you need to go buy one." in embed["description"]:
                    await self.bot.send("withdraw", amount="25k")
                    await self.bot.sub_send("shop", "buy", item="Shovel", quantity="1")
                elif "You don't have a fishing pole, you need to go buy one" in embed["description"]:
                    await self.bot.send("withdraw", amount="25k")
                    await self.bot.sub_send("shop", "buy", item="Fishing Pole", quantity="1")
                elif "You don't have a hunting rifle, you need to go buy one." in embed["description"]:
                    await self.bot.send("withdraw", amount="25k")
                    await self.bot.sub_send("shop", "buy", item="Hunting Rifle", quantity="1")
                elif "To start your streaming journey, you need following items:" in embed["description"]:
                    await self.bot.send("withdraw", amount="200k")
                    await self.bot.sub_send("shop", "buy", item="Keyboard", quantity="1")
                    await self.bot.sub_send("shop", "buy", item="Mouse", quantity="1")
            except KeyError:
                pass

            # Bank Rob
            try:
                if self.bankrob and "What do you want to do?" in embed["description"]:
                    await self.bot.click(message, 1, 0)
                    self.bankrob = False
            except KeyError:
                pass


async def setup(bot):
    await bot.add_cog(Autobuy(bot))
