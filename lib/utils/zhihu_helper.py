import sys
import datetime

reload(sys)
sys.setdefaultencoding('UTF8')


def get_format_date(timestamp):
    return datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')


def convert_to_csv(csv_file_name):
    pass