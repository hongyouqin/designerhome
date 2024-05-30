from typing import Union
import re

PROMPT_PREFIX = "<#"
PROMPT_SUFFIX = "#>"

USER_ID_PATTERN = f"{PROMPT_PREFIX}(\w+?){PROMPT_SUFFIX}"  # 用户ID正则表达式


def match_user_id(content: str) -> Union[str, None]:
    match = re.findall(USER_ID_PATTERN, content)
    if match[0] is not None:
        return match[0]
    else:
        return None