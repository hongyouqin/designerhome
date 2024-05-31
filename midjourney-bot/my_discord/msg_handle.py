from typing import Union
import re
from enum import Enum


PROMPT_PREFIX = "<#"
PROMPT_SUFFIX = "#>"

USER_ID_PATTERN = f"{PROMPT_PREFIX}(\w+?){PROMPT_SUFFIX}"  # 用户ID正则表达式

class TriggerStatus(Enum):
    START = "start"
    GEN = "generating" # 生成中
    END = "end"
    ERROR = "error" #生成错误

def match_user_id(content: str) -> Union[str, None]:
    """正则表达式提取用户ID

    Args:
        content (str): 文本内容

    Returns:
        Union[str, None]: 返回用户ID，或者None
    """
    match = re.findall(USER_ID_PATTERN, content)
    if match:
        return match[0]
    else:
        return None
    
    
    
