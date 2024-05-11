from discord import Intents, Message
from discord.ext import commands

intents =  Intents.default()
intents.message_content = True
discord_bot = commands.Bot(command_prefix="", intents=intents)

@discord_bot.event
async def on_read():
    pass

async def on_message(message):
    pass
