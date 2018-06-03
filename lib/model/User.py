import sys
from Question import Question
from lib.db.RedisHelper import redisHelper


reload(sys)
sys.setdefaultencoding('UTF8')


class User(object):
    def __init__(self, people):
        self.max_count = 50
        self.user_id = people.id
        print(self.user_id)
        self.user_name = people.name
        print(self.user_name)
        self.answer_time_list = self.get_answer_time_list(people)
        print(self.answer_time_list)
        self.article_time_list = self.get_article_time_list(people)
        print(self.article_time_list)
        self.crawl_comment_data(people)
        print("finish crawl comment data")
        self.favorite_column_list = self.get_favorite_column_list(people)
        for column in self.favorite_column_list:
            print(column)
        self.favorite_topic_list = self.get_favorite_topic_list(people)
        for topic in self.favorite_topic_list:
            print(topic)
        self.question_time_list = self.get_question_time_list(people)
        print(self.question_time_list)
        self.favorite_user_id_list = self.get_favorite_user_id_list(people)
        print(self.favorite_user_id_list)
        self.follower_user_id_list = self.get_follower_user_id_list(people)
        print(self.follower_user_id_list)
        self.live_time_list = self.get_live_time_list(people)
        print(self.live_time_list)
        self.thought_time_list = self.get_thought_time_list(people)
        print(self.thought_time_list)
        self.activity_time_list = self.get_activity_time_list(people)
        print(self.activity_time_list)

    def get_answer_time_list(self, people):
        time_set = set()
        count = 0
        for answer in people.answers:
            time_set.add(answer.created_time)
            time_set.add(answer.updated_time)
            count += 1
            if count > self.max_count:
                break
        return list(time_set)

    def get_article_time_list(self, people):
        time_set = set()
        count = 0
        for article in people.articles:
            time_set.add(article.updated_time)
            count += 1
            if count > self.max_count:
                break
        return list(time_set)

    def crawl_comment_data(self, people):
        print("question count: %d" % people.question_count)
        count = 0
        for question in people.questions:
            Question.handle(question)
            count += 1
            if count > self.max_count:
                break
        print("answer count: %d" % people.answer_count)
        count = 0
        for answer in people.answers:
            Question.handle_answer(answer)
            count += 1
            if count > self.max_count:
                break

    def get_comment_time_list(self):
        return redisHelper.get_user_comment(self.user_id)

    def get_favorite_column_list(self, people):
        column_list = []
        count = 0
        for favoriate_column in people.following_columns:
            column_list.append(favoriate_column.title)
            count += 1
            if count > self.max_count:
                break
        return column_list

    def get_favorite_topic_list(self, people):
        topic_list = []
        count = 0
        for favoriate_topic in people.following_topics:
            topic_list.append(favoriate_topic.name)
            count += 1
            if count > self.max_count:
                break
        return topic_list

    def get_question_time_list(self, people):
        time_set = set()
        count = 0
        for question in people.questions:
            time_set.add(question.created_time)
            time_set.add(question.updated_time)
            count += 1
            if count > self.max_count:
                break
        return list(time_set)

    def get_favorite_user_id_list(self, people):
        user_list = []
        count = 0
        for user in people.followings:
            user_list.append(user.id)
            count += 1
            if count > self.max_count:
                break
        return user_list

    def get_follower_user_id_list(self, people):
        user_list = []
        count = 0
        for user in people.followers:
            user_list.append(user.id)
            count += 1
            if count > self.max_count:
                break
        return user_list

    def get_live_time_list(self, people):
        time_list = []
        count = 0
        for live in people.lives:
            time_list.append(live.created_at)
            count += 1
            if count > self.max_count:
                break
        return time_list

    def get_thought_time_list(self, people):
        # NO API for this
        return []

    def get_activity_time_list(self, people):
        time_list = []
        count = 0
        for activity in people.activities:
            time_list.append(activity.created_time)
            count += 1
            if count > self.max_count:
                break
        return time_list

    def __str__(self):
        return "user_id = %s, user_name = %s, answer_time_list = %s, article_time_list = %s, favorite_column_list = " \
               "%s, favorite_topic_list = %s, question_time_list = %s, favorite_user_id_list = %s, " \
               "follower_user_id_list = %s, live_time_list = %s, thought_time_list = %s, activity_time_list = %s" % (
            str(self.user_id), str(self.user_name), str(self.answer_time_list), str(self.article_time_list),
            str(self.favorite_column_list), str(self.favorite_topic_list), str(self.question_time_list),
            str(self.favorite_user_id_list), str(self.follower_user_id_list), str(self.live_time_list),
            str(self.thought_time_list), str(self.activity_time_list))



