from guilded.ext import commands

from cogs.bot import Bot
from cogs.mod import Mod

import dotenv
import os

dotenv.load_dotenv()

bot = commands.Bot(user_id='mbbGvlVm', command_prefix='!.')

bot.add_cog(Bot(bot))
bot.add_cog(Mod(bot))

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')

bot.run(os.environ['TOKEN'])