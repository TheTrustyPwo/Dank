import asyncio
import random
import time

from discord.ext import commands, tasks


ITEMS = ["Lucky Horseshoe", "Pizza", "Ammo", "Fishing Bait"]

class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.item = 0

    async def cog_load(self):
        self.commands.start()

    @tasks.loop(seconds=0.05)
    async def commands(self):
        if self.bot.config["state"] is False or self.bot.lock:
            return
        for command in self.bot.commands_list:
            # Handled in cogs
            if command == "bj":
                continue
            if time.time() - self.bot.last_ran[command] < self.bot.commands_delay[command] or not self.bot.config["commands"][command]:
                continue
            if command == "use":
                await self.bot.send(self.bot.commands_list[command], item=ITEMS[self.item])
                self.item = (self.item + 1) % len(ITEMS)
                self.bot.last_ran[command] = time.time()
                await asyncio.sleep(0.5)
                continue
            if command == "dep_all":
                await self.bot.send(self.bot.commands_list[command], amount="max")
                self.bot.last_ran[command] = time.time()
                await asyncio.sleep(0.5)
                continue
            if command == "work":
                await self.bot.sub_send(self.bot.commands_list[command], "shift")
                self.bot.last_ran[command] = time.time()
                await asyncio.sleep(5)
                continue
            await self.bot.send(self.bot.commands_list[command])
            self.bot.last_ran[command] = time.time()
            await asyncio.sleep(0.5)
            return


async def setup(bot):
    await bot.add_cog(Commands(bot))
