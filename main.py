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


# This function is used to init the database, do not need to run every start time
def run_on_the_first_time():
    crawl_start_user_list = ["wu-hai-feng-70", "zhang-jia-wei"]
    for user_id in crawl_start_user_list:
        crawl_user_by_id(user_id)
    print("Prepare finished, start with queue size %d" % redisQueue.qsize())

# redisHelper.clean_all()
# run_on_the_first_time


def crawl_user_by_id(user_id):
    print("=" * 100)
    print("Crawl on user id %s" % user_id)
    try:
        people = client.people(user_id)
        user = User(people)
        redisHelper.save_user(user)
    except UnexpectedResponseException as ex:
        print("Exception happen when crawl on %s" % user_id)


def crawl_task():
    print("Start Crawl Task")
    user_id = redisQueue.get()
    print("Get user id %s" % user_id)
    crawl_user_by_id(user_id)


print("Starting crawl process with queue size %d" % redisQueue.qsize())
while not redisQueue.empty():
    print("start new process!")
    process = Process(target=crawl_task)
    process.daemon = True
    process.start()
    process.join()

