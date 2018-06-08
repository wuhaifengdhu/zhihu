import redis
import pickle
from lib.db.RedisPool import pool
from lib.db.RedisQueue import redisQueue


class RedisHelper(object):
    def __init__(self):
        self.redis = redis.Redis(connection_pool=pool)
        self.user_prefix = "U"
        self.question_prefix = "T"
        self.comment_prefix = "C"

    def save_user(self, user):
        self.redis.set(self.user_prefix + user.user_id, pickle.dumps(user))

    def get_user(self, user_id):
        user = self.redis.get(self.user_prefix + user_id)
        return pickle.loads(user)

    def export_all_users(self):
        for key in self.redis.scan_iter(self.user_prefix + "*"):
            user = pickle.loads(self.redis.get(key))
            print(user)

    def is_user_exist(self, user_id):
        return self.redis.get(self.user_prefix + user_id) is not None

    def is_question_exist(self, question_id, set_as_crawled=True):
        exist = False
        question_key = self.question_prefix + str(question_id)
        question = self.redis.get(question_key)
        if question is not None:
            exist = True
        elif set_as_crawled:
            self.redis.set(question_key, "Y")
        return exist

    def update_comments(self, user_id, create_time):
        comment_key = self.comment_prefix + user_id
        user_comment_str = self.redis.get(comment_key)
        if user_comment_str is None:
            user_comment_list = []
        else:
            user_comment_list = pickle.loads(user_comment_str)
        user_comment_list.append(create_time)
        self.redis.set(comment_key, pickle.dumps(user_comment_list))

    def collect_crawl_people(self, user_id):
        if not self.is_user_exist(user_id):
            print("add user id %s into queue for crawl next, redisQueue Size %d" % (user_id, redisQueue.qsize()))
            redisQueue.put(user_id)

    def get_next_people(self):
        while True:
            user_id = redisQueue.get(False)
            if user_id is None:
                return None
            if not self.is_user_exist(user_id):
                return user_id

    def get_user_comment(self, user_id):
        comment_key = self.comment_prefix + user_id
        user_comment_str = self.redis.get(comment_key)
        if user_comment_str is None:
            user_comment_list = []
        else:
            user_comment_list = pickle.loads(user_comment_str)
        return user_comment_list

    def clean_all(self):
        for key in self.redis.keys(pattern='*'):
            self.redis.delete(key)


redisHelper = RedisHelper()

if __name__ == '__main__':
    redisHelper.clean_all()
    redis = redis.Redis(connection_pool=pool)
    for key in redis.keys(pattern='*'):
        print(key)
