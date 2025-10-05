from guilded.ext import commands
import guilded

class Admin(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def reload(self, ctx: commands.Context, cog: str):
        try:
            self.bot.unload_extension(f'cogs.{cog}')
            self.bot.load_extension(f'cogs.{cog}')
            await ctx.send(f'Reloaded cog: {cog}')
        except Exception as e:
            await ctx.send(f'Error reloading cog {cog}: {e}')

    @commands.command()
    @commands.is_owner()
    async def load(self, ctx: commands.Context, cog: str):
        try:
            self.bot.load_extension(f'cogs.{cog}')
            await ctx.send(f'Loaded cog: {cog}')
        except Exception as e:
            await ctx.send(f'Error loading cog {cog}: {e}')

def setup(bot: commands.Bot):
    bot.add_cog(Admin(bot))