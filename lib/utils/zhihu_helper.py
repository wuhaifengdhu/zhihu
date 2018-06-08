import sys
import datetime
from lib.db.RedisHelper import redisHelper
from lib.db.RedisQueue import redisQueue

reload(sys)
sys.setdefaultencoding('UTF8')


def get_format_date(timestamp):
    return datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')


def print_all_users():
    redisHelper.export_all_users()


def print_queue():
    print("current queue size: %d" % redisQueue.qsize())


if __name__ == '__main__':
    print_queue()
