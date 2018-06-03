import sys
from threading import Thread
from lib.db.RedisQueue import redisQueue
from lib.db.RedisHelper import redisHelper
from lib.client.Client import client
from lib.model.User import User

reload(sys)
sys.setdefaultencoding('UTF8')


class Crawler(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True

    def run(self):
        user_id = redisQueue.get(False)
        user = User(client.people(user_id))
        redisHelper.save_user(user)
        print(user)


