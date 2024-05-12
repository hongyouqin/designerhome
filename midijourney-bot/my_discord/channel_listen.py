from discord import Intents, Message
from discord.ext import commands
from loguru import logger

intents = Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="", intents=intents)


@bot.event
async def on_read():
    logger.debug(f"Logged in as {bot.user} (ID: {bot.user.id})")
    pass


@bot.event
async def on_message(message: Message):
    pass


@bot.event
async def on_message_edit(before, after):
    """
    处理敏感词
    """
    pass


@bot.event
async def on_message_delete(message):
    pass
