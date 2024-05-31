from discord import Message
import nsq


def pub_message(use_id: str, status: str, message: Message):
    """_summary_

    Args:
        use_id (str): 用户id
        status (str): 状态
        message (Message): 消息
    """