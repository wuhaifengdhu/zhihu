# -*- coding:utf-8 -*-
import sqlite3
import cPickle as pickle


class User(object):
    def __init__(self, name):
        self.name = name
        self.body = [name, name]


class DbTest(object):
    def __init__(self, db_file="test.db"):
        self.__connector = sqlite3.connect(db_file)
        self.__cursor = self.__connector.cursor()
        self.create_table_if_not_exist()

    def create_table_if_not_exist(self):
        self.__cursor.execute('''CREATE TABLE IF NOT EXISTS table_users
                      (user_id text primary key, user_data blob)''')
        self.__connector.commit()

    def test_write(self, user):
        try:
            self.__cursor.execute('INSERT INTO table_users(user_id, user_data) values(?, ?)', (user.name, sqlite3.Binary(pickle.dumps(user, protocol=2))))
            self.__connector.commit()
        except Exception as ex:
            print("Exception happen when insert into table, user_str=%s" % user.name)


    def test_read(self):
        self.__cursor.execute("select user_data from table_users")
        users = self.__cursor.fetchall()
        if users:
            print("length: %d" % len(users))
            print(users[0])
            return [pickle.loads(str(user[0])) for user in users]
        else:
            return []


if __name__ == '__main__':
    dbTest = DbTest()
    dbTest.test_write(User(u'吴海峰'))
    dbTest.test_write(User(u'画画'))
    users = dbTest.test_read()
    for user in users:
        print(user.name)
        for body in user.body:
            print(body)


