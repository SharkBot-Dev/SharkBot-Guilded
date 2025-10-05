from guilded.ext import commands
import guilded

class Bot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def about(self, ctx: commands.Context):
        await ctx.send("This bot was created by guilded.py.")

    @commands.command()
    async def help(self, ctx: commands.Context):
        await ctx.reply(embed=guilded.Embed(
            title="Help",
            description="Available commands:\n"
                        "!.about - Information about the bot\n"
                        "!.help - Display this help message\n"
                        "!.kick <member> - Kick a member (requires permissions)\n"
                        "!.ban <user> [reason] - Ban a user (requires permissions)",
            color=guilded.Color.green()
        ))

def setup(bot: commands.Bot):
    bot.add_cog(Bot(bot))