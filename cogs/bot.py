from guilded.ext import commands

class Bot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def about(self, ctx: commands.Context):
        await ctx.send("This bot was created by guilded.py.")

def setup(bot: commands.Bot):
    bot.add_cog(Bot(bot))