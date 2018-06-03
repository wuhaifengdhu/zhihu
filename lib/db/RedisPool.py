import sys
import redis

reload(sys)
sys.setdefaultencoding('UTF8')

pool = redis.ConnectionPool(host='wudevin.com', port=6379)