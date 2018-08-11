import sys

from lib.utils.zhihu_helper import ZhihuCrawler


reload(sys)
sys.setdefaultencoding('UTF8')


class Main(object):
    def __init__(self):
        self.crawler = ZhihuCrawler(50)

    def run_crawl(self):
        self.crawler.run_crawl()

    def show_crawled_data(self):
        self.crawler.print_all_users()

    def run_only_one_time(self):
        self.crawler.initialize()

    def print_date(self, unix_time):
        print(self.crawler.get_format_date(unix_time))

    def show_total_records_number(self):
        print("Total records crawled: %d" % self.crawler.get_total_records_number())


if __name__ == '__main__':
    main = Main()
    # main.run_crawl()
    main.show_total_records_number()
    # main.show_crawled_data()


