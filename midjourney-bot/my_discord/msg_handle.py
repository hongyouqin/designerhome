from typing import Union
import re
from enum import Enum
from discord import Message
from my_discord.msg_nsq import NsqMsg
from my_discord.msg import TopicData, Attachment
from config import ConfigManager
from loguru import logger


PROMPT_PREFIX = "<#"
PROMPT_SUFFIX = "#>"
MSG_TOPIC = "mj_channel_topic"

USER_ID_PATTERN = f"{PROMPT_PREFIX}(\w+?){PROMPT_SUFFIX}"  # 用户ID正则表达式


class TriggerStatus(Enum):
    START = "start"
    GEN = "generating"  # 生成中
    END = "end"
    ERROR = "error"  # 生成错误


def match_user_id(content: str) -> Union[str, None]:
    match = re.findall(USER_ID_PATTERN, content)
    if match:
        return match[0]
    else:
        return None


async def write_message_to_nsq(user_id: str, status: str, message: Message):
    # 获取nsq_msg单例实例
    cfg = ConfigManager.get_cfg()
    addresses = cfg["nsq"]["addresses"]
    nsq_msg = NsqMsg(addresses)
    topic = TopicData(
        user_id=user_id,
        status=status,
        content=message.content,
        attachments=[
            Attachment(**attachment.to_dict()) for attachment in message.attachments
        ],
        message_id=message.id,
    )
    topic_json = topic.to_dict()
    logger.debug(topic_json)
    nsq_msg.pub_message(MSG_TOPIC, topic_json)
