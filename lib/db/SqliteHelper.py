# -*- coding:utf-8 -*-
import sqlite3
import cPickle as pickle


class SqliteHelper(object):
    def __init__(self, db_file="zhihu.db"):
        self.__connector = sqlite3.connect(db_file)
        self.__cursor = self.__connector.cursor()
        self.create_table_if_not_exist()

    def create_table_if_not_exist(self):
        print("Init db if not exist")
        self.__cursor.execute('''CREATE TABLE IF NOT EXISTS user_waiting_crawl
              (user_id text primary key)''')
        self.__cursor.execute('''CREATE TABLE IF NOT EXISTS table_users
                      (user_id text primary key, user_data blob)''')
        self.__cursor.execute('''CREATE TABLE IF NOT EXISTS question_crawled
                              (question_id int primary key)''')
        self.__cursor.execute('''CREATE TABLE IF NOT EXISTS table_comments
                                      (user_id text primary key, comments_update blob)''')
        self.commit()

    def close(self):
        self.commit()
        self.__connector.close()

    def commit(self):
        self.__connector.commit()

    def save_user(self, user):
        try:
            self.__cursor.execute('''INSERT INTO table_users(user_id, user_data) values(?, ?)''', (user.user_id, sqlite3.Binary(pickle.dumps(user, protocol=2))))
            self.commit()
        except UnicodeDecodeError as err:
            print("Error when save %s" % user.user_id)
        except Exception as ex:
            print("Exception happen when insert into table, user name=%s" % user.user_name)

    def get_user(self, user_id):
        self.__cursor.execute('''SELECT user_data from table_users where table_users.user_id=?''',  (user_id,))
        user = self.__cursor.fetchone()
        if user is not None:
            return pickle.loads(str(user[0]))
        else:
            return None

    def export_all_users(self):
        self.__cursor.execute('''SELECT user_data from table_users''')
        users = self.__cursor.fetchall()
        if users:
            print("length: %d" % len(users))
            return [pickle.loads(str(user[0])) for user in users]
        else:
            return []

    def get_records_number(self):
        self.__cursor.execute('''SELECT COUNT(*) from table_users''')
        count = self.__cursor.fetchone()[0]
        return count

    def is_user_exist(self, user_id):
        self.__cursor.execute('''SELECT COUNT(*) from table_users where user_id = ? ''', (user_id,))
        count = self.__cursor.fetchone()[0]
        return count > 0

    def is_question_exist(self, question_id, set_as_crawled=True):
        self.__cursor.execute('''SELECT COUNT(*) from question_crawled where question_id=? ''',  (question_id,))
        count = self.__cursor.fetchone()[0]
        return count > 0

    def update_comments(self, user_id, create_time):
        user_comment_list = self.get_user_comment(user_id)
        user_comment_list.append(create_time)
        self.__cursor.execute('''UPDATE table_comments set comments_update=? where user_id=? ''', (sqlite3.Binary(pickle.dumps(user_comment_list, protocol=2)), user_id))

    def get_user_comment(self, user_id):
        self.__cursor.execute('''SELECT comments_update from table_comments where user_id=? ''',  (user_id,))
        user_comment_str_list = self.__cursor.fetchone()
        if user_comment_str_list is None or len(user_comment_str_list) == 0:
            user_comment_list = []
        else:
            user_comment_list = pickle.loads(str(user_comment_str_list[0]))
        return user_comment_list


sqlite_helper = SqliteHelper()


if __name__ == '__main__':
    pass
