from my_discord.msg import TopicData
import nsq
import tornado.ioloop
from queue import Queue, Empty
from loguru import logger


class NsqMsg:
    """nsq单例模式，用于消息投递"""

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(NsqMsg, cls).__new__(cls)
            logger.info("nsq 单例模式初始化")
        return cls._instance

    def __init__(self, addresses) -> None:
        self.write = nsq.Writer(addresses)
        self.queue = Queue()
        self.loop = tornado.ioloop.IOLoop.current()

    def pub_message(self, topic: str, data: TopicData):
        """推送数据到消息队列上去

        Args:
            data (TopicData) pub
        """
        self.queue.put((topic, data))
        self.loop.add_callback(self._pub_msg_next)

    def _pub_msg_next(self):
        try:
            topic, message = self.queue.get_nowait()
        except Empty:
            return

        def callback(conn, data):
            logger.info(f"msg pub: {data}")
            self.loop.add_callback(self._pub_msg_next)

        try:
            self.write.pub(topic, message.encode(), callback)
        except Exception as e:
            logger.error(f"Failed to publish message: {e}")
            self.loop.add_callback(self._pub_msg_next)

    def start(self):
        self.loop.start()

    def stop(self):
        self.loop.stop()
