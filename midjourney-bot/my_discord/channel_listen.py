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
    logger.debug(f"on_message content: {message.content}")
    pass


@bot.event
async def on_message_edit(before: Message, after: Message):
    """
    处理敏感词
    """
    logger.debug(f"on_message_edit before content: {before.content}")
    logger.debug(f"on_message_edit after content: {before.content}")
    pass


@bot.event
async def on_message_delete(message):
    logger.debug(f"on_message_delete content: {message.content}")
    pass
