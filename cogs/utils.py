from discord.ext import commands


class Utils(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="bal")
    async def balance(self, ctx):
        channel = ctx.channel
        await self.bot.send("balance", channel=channel)

    @commands.command(name="inv")
    async def inventory(self, ctx):
        channel = ctx.channel
        await self.bot.send("inventory", channel=channel)

    @commands.command(name="p")
    async def profile(self, ctx):
        channel = ctx.channel
        await self.bot.send("profile", channel=channel)


async def setup(bot):
    await bot.add_cog(Utils(bot))
