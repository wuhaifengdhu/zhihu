# -*- coding:utf-8 -*-
import sys
import datetime
from lib.utils.zhihu_helper import crawl
from lib.client.Client import client
from lib.utils.csv_helper import CsvHelper
from lib.db.SqliteHelper import sqlite_helper
from lib.model.User import User


reload(sys)
sys.setdefaultencoding('UTF8')


class Main(object):
    @staticmethod
    def verify_client():
        p = client.people("wu-hai-feng-70")
        if p is not None:
            print("Client verified OK!")
        else:
            print("Client verified Failed!")

    @staticmethod
    def run_crawl():
        crawl.run_crawl()
        crawl.finished()

    @staticmethod
    def export_csv_file(output_file_name):
        user_data = []
        for user in crawl.export_all_users():
            user_str_list = user.to_list(sqlite_helper)
            print(user_str_list)
            user_data.append(user_str_list)
        CsvHelper.write_list_to_csv(output_file_name, User.get_fields(), user_data)

    @staticmethod
    def show_total_records_number():
        print("Total records crawled: %d" % crawl.get_total_records_number())


if __name__ == '__main__':
    Main.verify_client()
    # Main.run_crawl()
    Main.show_total_records_number()
    Main.export_csv_file("crawled_data.csv")
    sqlite_helper.close()



