import sqlite3
import pickle


class SqliteHelper(object):
    def __init__(self, db_file="./data/zhihu.db"):
        self.__connector = sqlite3.connect(db_file)
        self.__cursor = self.__connector.cursor()
        self.create_table_if_not_exist()

    def create_table_if_not_exist(self):
        print("Init db if not exist")
        self.__cursor.execute('''CREATE TABLE IF NOT EXISTS user_waiting_crawl
              (user_id text primary key)''')
        self.__cursor.execute('''CREATE TABLE IF NOT EXISTS table_users
                      (user_id text primary key, user_data text)''')
        self.__cursor.execute('''CREATE TABLE IF NOT EXISTS question_crawled
                              (question_id int primary key)''')
        self.__cursor.execute('''CREATE TABLE IF NOT EXISTS table_comments
                                      (user_id text primary key, comments_update text)''')
        self.commit()

    def close(self):
        self.commit()
        self.__connector.close()

    def commit(self):
        self.__connector.commit()

    def save_user(self, user):
        self.__cursor.execute("INSERT INTO table_users values(%s, %s)" % (user.user_id, pickle.dumps(user)))

    def get_user(self, user_id):
        self.__cursor.execute("SELECT * from table_users where table_users.user_id=%s" % user_id)
        user = self.__cursor.fetchone()
        if user is not None:
            return pickle.loads(user[0].user_data)
        else:
            return None

    def export_all_users(self):
        self.__cursor.execute("SELECT * from table_users")
        users = self.__cursor.fetchall()
        if users:
            return [pickle.loads(user[0].user_data) for user in users]
        else:
            return None

    def get_records_number(self):
        self.__cursor.execute("SELECT COUNT(*) from table_users")
        count = self.__cursor.fetchone()[0]
        return count

    def is_user_exist(self, user_id):
        self.__cursor.execute("SELECT COUNT(*) from table_users where table_users.user_id=?", user_id)
        count = self.__cursor.fetchone()[0]
        return count > 0

    def is_question_exist(self, question_id, set_as_crawled=True):
        self.__cursor.execute("SELECT COUNT(*) from question_crawled where question_id=%d" % question_id)
        count = self.__cursor.fetchone()[0]
        return count > 0

    def update_comments(self, user_id, create_time):
        self.__cursor.execute("SELECT * from table_comments where user_id=%s" % user_id)
        user_comment_str = self.__cursor.fetchone()[0]
        if user_comment_str is None:
            user_comment_list = []
        else:
            user_comment_list = pickle.loads(user_comment_str)
        user_comment_list.append(create_time)
        self.__cursor.execute("UPDATE table_comments set comments_update=%s where user_id=%s" % (pickle.dumps(user_comment_list), user_id))

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


if __name__ == '__main__':
    db_helper = SqliteHelper()
    db_helper.close()

