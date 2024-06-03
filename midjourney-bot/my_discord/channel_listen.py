from discord import Intents, Message
from discord.ext import commands
from loguru import logger
from my_discord.msg_handle import match_user_id, TriggerStatus, write_message_to_nsq

intents = Intents.default()
intents.message_content = True
intents.messages = True
bot = commands.Bot(command_prefix="", intents=intents)


@bot.event
async def on_ready():
    logger.debug(f"Logged in as {bot.user} (ID: {bot.user.id})")
    


@bot.event
async def on_message(message: Message):
    if message.author == bot.user:
        logger.debug(f"on_message owner: {bot.user}")
        return
    user_id = match_user_id(message.content)
    if user_id is None:
        logger.error(f"on_message The msg={message.content} format is not true.")
        return
    if message.content.find("Waiting to start") != -1:
        status = TriggerStatus.START
    elif message.content.find("(Stopped)") != -1:
        status = TriggerStatus.ERROR
    else:
        status = TriggerStatus.END
    logger.debug(f"on_message status={status} content: {message.content}")
    await write_message_to_nsq(user_id, status, message)


@bot.event
async def on_message_edit(before: Message, after: Message):
    """
    消息改变时，触发
    """
    logger.debug(f"on_message_edit before content: {before.content}")
    logger.debug(f"on_message_edit after content: {before.content}")
    if after.author == bot.user:
        logger.debug(f"on_message_edit owner: {bot.user}")
        return
    user_id = match_user_id(after.content)
    if user_id is None:
        logger.error(f" on_message_edit The msg={after.content} format is not true.")
        return
    status = TriggerStatus.GEN
    await write_message_to_nsq(user_id, status, after)

@bot.event
async def on_message_delete(message: Message):
    logger.debug(f"on_message_delete content: {message.content}")
