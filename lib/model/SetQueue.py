# -*- coding:utf-8 -*-
from lib.utils.store_helper import StoreHelper
from Queue import Queue


class SetQueue(object):
    def __init__(self, auto_save_size=1000):
        self.__store_filename = "waiting_crawl.dat"
        self.__default_set = {"zhu-yue-86-84"}
        self.full_set = StoreHelper.load_data(self.__store_filename, self.__default_set)
        print("Waiting crawl list when start: %d" % self.qsize())
        self.__add_count = 0
        self.__threshold = auto_save_size

    def add(self, item):
        self.__add_count += 1
        self.full_set.add(item)
        if self.__add_count > self.__threshold:
            self.save()
            self.reset_count()

    def get(self):
        return self.full_set.pop()

    def reset_count(self):
        self.__add_count = 0

    def save(self):
        print("Waiting crawl list: auto save, current waiting crawl list size: %d" % self.qsize())
        StoreHelper.store_data(self.full_set, self.__store_filename)

    def empty(self):
        return self.qsize() == 0

    def qsize(self):
        return len(self.full_set)


waiting_crawl_queue = SetQueue()


if __name__ == "__main__":
    testQueue = SetQueue(10)
    print(testQueue)
    for i in xrange(100, 200):
        testQueue.add("%d" % i)
    print(testQueue)











