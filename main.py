import sys
import time
from random import randint

from zhihu_oauth import UnexpectedResponseException

from lib.client.Client import client
from lib.model.User import User
from multiprocessing import Process
from lib.db.RedisQueue import redisQueue
from lib.db.RedisHelper import redisHelper


reload(sys)
sys.setdefaultencoding('UTF8')

total_process = 0


redisHelper.clean_all()


def crawl_user_by_id(user_id):
    print("=" * 100)
    print("Crawl on user id %s" % user_id)
    people = client.people(user_id)
    User(people)


def crawl_task():
    crawl_user_by_id(redisQueue.get())


crawl_start_user_list = ["wu-hai-feng-70", "zhang-jia-wei"]
for user_id in crawl_start_user_list:
    try:
        crawl_user_by_id(user_id)
    except UnexpectedResponseException as ex:
        print("Exception happen when crawl on %s" % user_id)

print(redisQueue.qsize())
while not redisQueue.empty():
    process = Process(target=crawl_task)
    # process.daemon = True
    process.start()
    process.join()
    print("start to sleep!")
    time.sleep(randint(0, 7))
    print("after sleep!")
