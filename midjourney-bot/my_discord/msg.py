from typing import TypedDict, List


class Attachment(TypedDict):
    """这里面是存的关于下载的mj图片信息"""

    id: int
    url: str
    proxy_url: str
    filename: str
    content_type: str
    width: int
    height: int
    size: int
    ephemeral: bool


class TopicData:
    """消息主题数据"""

    use_id: str
    status: str
    content: str
    attachments: List[Attachment]
    message_id: str
