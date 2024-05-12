import tomli
from loguru import logger


def load_cfg(file_path: str):
    try:
        with open(file_path, "rb") as file:
            config_data = tomli.load(file)
        return config_data
    except Exception as e:
        logger.exception(f"读取文件发生异常:{e}")
