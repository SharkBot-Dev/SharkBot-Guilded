from guilded.ext import commands
import guilded

class Info(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def user(self, ctx: commands.Context, userid: str):
        try:
            User = await self.bot.fetch_user(userid)
            if not User:
                await ctx.send("User not found.")
                return
            
            embed = guilded.Embed(title=f"User Info", color=guilded.Color.green())
            embed.add_field(name="ID", value=User.id, inline=False)
            embed.add_field(name="Name", value=User.name, inline=False)
            embed.add_field(name="Bot", value="Yes" if User.bot else "No", inline=False)
            embed.set_thumbnail(url=User.avatar.url)
            await ctx.send(embed=embed)

        except Exception:
            await ctx.send(f"User not found.")
            return

def setup(bot: commands.Bot):
    bot.add_cog(Info(bot))