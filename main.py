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


if __name__ == '__main__':
    main = Main()
    # main.run_only_one_time()
    # main.run_crawl()
    # main.show_crawled_data()
    answer_time_list = [1526743488, 1528299812, 1520784517, 1510760551, 1510760524, 1513766668, 1528250381, 1518624913,
                        1513659092, 1527755578, 1524733498]
    for time_stamp in answer_time_list:
        main.print_date(time_stamp)


