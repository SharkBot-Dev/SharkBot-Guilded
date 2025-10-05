from guilded.ext import commands
import guilded

class Mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_server_permissions(kick_members=True)
    async def kick(self, ctx: commands.Context, member: guilded.Member):
        await ctx.guild.kick(member)
        await ctx.send(f'Kicked {member.name}.')

    @commands.command()
    @commands.has_server_permissions(ban_members=True)
    async def ban(self, ctx: commands.Context, user: guilded.User, reason: str = None):
        await ctx.guild.ban(user, reason=reason)
        await ctx.send(f'Banned {user.name}.')

def setup(bot: commands.Bot):
    bot.add_cog(Mod(bot))