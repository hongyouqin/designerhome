from loguru import logger
from my_discord import bot
from config import load_cfg
from dotenv import load_dotenv
from os import getenv

# 加载环境
load_dotenv()
cfg_path = getenv("CONFIG_FILE_PATH")
cfg = load_cfg(cfg_path)

if __name__ == "__main__":

    # 读取配置
    log_name = cfg["logger"]["name"]
    log_size = cfg["logger"]["size"]
    log_level = cfg["logger"]["level"]
    print(f"log name={log_name}; size={log_size}; level = {log_size}")

    # 设置日志格式
    logger.add(
        log_name, format="{time} {level} {message}", rotation=log_size, level=log_level
    )
    bot_token = cfg["bot"]["bot_token"]
    print(f"log name=")
    bot.run(bot_token)
