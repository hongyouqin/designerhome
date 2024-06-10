from typing import TypedDict, List
from dataclasses import dataclass
import json


@dataclass
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


@dataclass
class TopicData:
    """消息主题数据"""

    user_id: str
    status: str
    content: str
    attachments: List[Attachment]
    message_id: str

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "status": self.status,
            "content": self.content,
            "attachments": self.attachments,
            "message_id": self.message_id,
        }

    def to_json(self):
        return json.dumps(self.to_dict())
