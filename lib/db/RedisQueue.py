import sys
import redis
from lib.db.RedisPool import pool

reload(sys)
sys.setdefaultencoding('UTF8')


class RedisQueue(object):
    """Simple Queue with Redis Backend"""
    def __init__(self):
        self.__db = redis.Redis(connection_pool=pool)
        self.key = "queue"

    def qsize(self):
        """Return the approximate size of the queue."""
        return self.__db.llen(self.key)

    def empty(self):
        """Return True if the queue is empty, False otherwise."""
        return self.qsize() == 0

    def put(self, item):
        """Put item into the queue."""
        self.__db.rpush(self.key, item)

    def get(self, block=True, timeout=None):
        """Remove and return an item from the queue.

        If optional args block is true and timeout is None (the default), block
        if necessary until an item is available."""
        if block:
            item = self.__db.blpop(self.key, timeout=timeout)
        else:
            item = self.__db.lpop(self.key)

        if item:
            item = item[1]
        return item

    def get_nowait(self):
        """Equivalent to get(False)."""
        return self.get(False)


redisQueue = RedisQueue()


if __name__ == '__main__':
    redisQueue.put("a3a21d90b6a1cd2823579b7db5a18a0a")
    redisQueue.put("466ba048c3949d961139c42600ca58e3")
    redisQueue.put("76ac03c3d449e98cbbc7f5d1a6703906")
    print(redisQueue.get())
    print(redisQueue.qsize())
    print(redisQueue.get())
    print(redisQueue.qsize())
    print(redisQueue.get())
    print(redisQueue.qsize())
