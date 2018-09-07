import sys
from zhihu_oauth import UnexpectedResponseException
from lib.client.Client import client
from lib.db.SqliteHelper import sqlite_helper
from lib.model.SetQueue import waiting_crawl_queue
from lib.model.User import User

reload(sys)
sys.setdefaultencoding('UTF8')


class ZhihuCrawler(object):
    @staticmethod
    def crawl_task():
        user_id = waiting_crawl_queue.get()
        print("Crawl on user id %s, waiting crawl queue size %d, crawled size %d" % (user_id, waiting_crawl_queue.qsize(), sqlite_helper.get_records_number()))
        if user_id is not None and not sqlite_helper.is_user_exist(user_id):
            try:

                people = client.people(user_id)
                user = User(people, sqlite_helper)
                sqlite_helper.save_user(user)
            except UnexpectedResponseException as ex:
                print("Exception happen when crawl on %s" % user_id)
        else:
            print("User(%s) already in DB, avoid duplicate crawl" % user_id)

    @staticmethod
    def run_crawl():
        print("Starting run crawl with crawled size %d" % sqlite_helper.get_records_number())
        print("Starting run crawl with queue size %d" % waiting_crawl_queue.qsize())
        while not waiting_crawl_queue.empty():
            ZhihuCrawler.crawl_task()
            # ZhihuCrawler.crawl_task()
            # process = Thread(target=ZhihuCrawler.crawl_task)
            # process.daemon = True
            # process.start()
            # taskQueue.add_job(process)
            # time.sleep(10)

    @staticmethod
    def export_all_users():
        return sqlite_helper.export_all_users()

    @staticmethod
    def get_total_records_number():
        return sqlite_helper.get_records_number()

    @staticmethod
    def print_task_queue_size(self):
        print("current queue size: %d" % waiting_crawl_queue.qsize())

    @staticmethod
    def finished():
        sqlite_helper.close()


crawl = ZhihuCrawler()


if __name__ == '__main__':
    pass

