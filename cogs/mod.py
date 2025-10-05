from guilded.ext import commands
import guilded
import asyncio

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

    @commands.command()
    @commands.has_server_permissions(ban_members=True)
    async def unban(self, ctx: commands.Context, user: guilded.User):
        await ctx.guild.unban(user)
        await ctx.send(f'UnBanned {user.name}.')

    @commands.command()
    @commands.has_server_permissions(administrator=True)
    async def clear(self, ctx: commands.Context, count: int):
        if count < 1 or count > 15:
            await ctx.send('Please provide a number between 1 and 15.')
            return
        for m in await ctx.channel.history(limit=count + 1):
            await m.delete()
            await asyncio.sleep(0.8)
        await ctx.send(f'Cleared {count} messages.', delete_after=5)

def setup(bot: commands.Bot):
    bot.add_cog(Mod(bot))