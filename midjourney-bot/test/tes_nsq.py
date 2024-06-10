import nsq
import tornado.ioloop
import time


def pub_message():
    message = time.strftime("%H:%M:%S").encode("utf-8")  # Encode the message to bytes
    writer.pub("test", message, finish_pub)


def finish_pub(conn, data):
    print(data)


writer = nsq.Writer(["47.101.161.124:9912"])
tornado.ioloop.PeriodicCallback(pub_message, 1000).start()
nsq.run()
