from guilded.ext import commands
import guilded

class Bot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener('on_command_error')
    async def on_command_error(self, ctx: commands.Context, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please provide all required arguments.")
        elif isinstance(error, commands.CommandNotFound):
            await ctx.send("This command does not exist.")
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send("You do not have the required permissions to use this command.")
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.send("I do not have the required permissions to execute this command.")
        else:
            print(f'Error: {error}')
            await ctx.send("An error occurred while processing the command.")

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
                        "!.ban <user> [reason] - Ban a user (requires permissions)\n"
                        "!.unban <user_id> - Unban a user (requires permissions)\n"
                        "!.clear <count> - Clear messages (requires permissions)\n"
                        "!.user [userid] - Get information about a user\n"
                        "!.roll [sides] - Roll a dice with specified sides (default is 6)\n",
            color=guilded.Color.green()
        ))

def setup(bot: commands.Bot):
    bot.add_cog(Bot(bot))