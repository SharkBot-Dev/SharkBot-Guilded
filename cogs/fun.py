from guilded.ext import commands
import guilded
import asyncio
import random

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def roll(self, ctx: commands.Context, sides: int = 6):
        if sides < 1:
            await ctx.send("Please provide a positive integer for the number of sides.")
            return
        result = random.randint(1, sides)
        await ctx.send(f'You rolled a {result} on a {sides}-sided dice.')

def setup(bot: commands.Bot):
    bot.add_cog(Fun(bot))