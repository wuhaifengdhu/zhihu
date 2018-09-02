# -*- coding:utf-8 -*-
import sys
import datetime
from lib.utils.zhihu_helper import crawl
from lib.client.Client import client


reload(sys)
sys.setdefaultencoding('UTF8')


class Main(object):
    @staticmethod
    def verify_client():
        p = client.people("wu-hai-feng-70")
        print(p)

    @staticmethod
    def run_crawl():
        crawl.run_crawl()
        crawl.finished()

    @staticmethod
    def show_crawled_data(self):
        for user in crawl.export_all_users():
            print(user)

    @staticmethod
    def print_date(unix_time):
        print(datetime.datetime.fromtimestamp(unix_time).strftime('%Y-%m-%d %H:%M:%S'))

    @staticmethod
    def show_total_records_number():
        print("Total records crawled: %d" % crawl.get_total_records_number())


if __name__ == '__main__':
    Main.verify_client()
    Main.run_crawl()
    Main.show_total_records_number()
    Main.show_crawled_data()



