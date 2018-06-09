import sys
import datetime
from multiprocessing import Process

from zhihu_oauth import UnexpectedResponseException

from lib.client.Client import client
from lib.db.RedisHelper import redisHelper
from lib.db.RedisQueue import redisQueue
from lib.model.TaskQueue import TaskQueue
from lib.model.User import User

reload(sys)
sys.setdefaultencoding('UTF8')


class ZhihuCrawler(object):
    def __init__(self, max_thread_number):
        self.__max_thread_number = max_thread_number
        self.__process_queue = TaskQueue(self.__max_thread_number)

    @staticmethod
    def __crawl_user_by_id(user_id):
        print("=" * 100)
        print("Crawl on user id %s" % user_id)
        try:
            people = client.people(user_id)
            user = User(people)
            redisHelper.save_user(user)
        except UnexpectedResponseException as ex:
            print("Exception happen when crawl on %s" % user_id)

    def __crawl_task(self):
        print("Start Crawl Task")
        user_id = redisQueue.get()
        print("Get user id %s" % user_id)
        self.__crawl_user_by_id(user_id)

    def run_crawl(self):
        print("Starting crawl process with queue size %d" % redisQueue.qsize())
        while not redisQueue.empty():
            print("start new process! Current task queue size %d" % redisQueue.qsize())
            process = Process(target=self.__crawl_task)
            process.daemon = True
            process.start()
            self.__process_queue.add_job(process)

    # This function is used to init the database, do not need to run every start time
    def initialize(self):
        # Clean all data in data base
        # redisHelper.clean_all()
        # Start crawl from two provided users
        crawl_start_user_list = ["wu-hai-feng-70", "zhang-jia-wei"]
        for user_id in crawl_start_user_list:
            self.__crawl_user_by_id(user_id)
        print("Prepare finished, start with queue size %d" % redisQueue.qsize())

    @staticmethod
    def get_format_date(timestamp):
        return datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

    @staticmethod
    def print_all_users():
        redisHelper.export_all_users()

    @staticmethod
    def print_task_queue_size(self):
        print("current queue size: %d" % redisQueue.qsize())


crawl = ZhihuCrawler(50)


if __name__ == '__main__':
    print(crawl.get_format_date(1526874368))

