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


if __name__ == '__main__':
    main = Main()
    main.run_crawl()



