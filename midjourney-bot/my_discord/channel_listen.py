from discord import Intents, Message
from discord.ext import commands
from loguru import logger
from my_discord.msg_handle import (
    match_user_id,
    TriggerStatus
)

intents = Intents.default()
intents.message_content = True
intents.messages = True
bot = commands.Bot(command_prefix="", intents=intents)


@bot.event
async def on_ready():
    logger.debug(f"Logged in as {bot.user} (ID: {bot.user.id})")
    pass


@bot.event
async def on_message(message: Message):
    if message.author == bot.user:
        logger.debug(f"on_message owner: {bot.user}")
        return
    user_id = match_user_id(message.content)
    if user_id is None:
        logger.error(f"The msg={message.content} format is not true.")
        return
    if message.content.find("Waiting to start") != -1:
        status = TriggerStatus.START
    elif message.content.find("(Stopped)") != -1:
         status = TriggerStatus.ERROR
    else:
        status = TriggerStatus.END
    logger.debug(f"on_message status={status} content: {message.content}")
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
