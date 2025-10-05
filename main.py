from guilded.ext import commands

import dotenv
import os

dotenv.load_dotenv()

bot = commands.Bot(user_id='mbbGvlVm', command_prefix='!.', help_command=None, owner_id='dKnXkYB4')

for cog in os.listdir('./cogs'):
    if cog.endswith('.py'):
        bot.load_extension(f'cogs.{cog[:-3]}')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')

bot.run(os.environ['TOKEN'])