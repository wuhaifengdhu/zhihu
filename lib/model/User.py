# 用户id、
# 该用户的回答时间list、
# 发表的文章时间list、
# 评论的时间list，
# 该用户关注的专栏、
# 该用户关注的话题、
# 问题时间list、
# 关注了的人的id list、
# 以及关注他的人的id list、
# 用户知乎live时间list、
# 他的文章的时间的list
# 他的想法的时间list


class User(object):
    def __init__(self, people):
        self.user_id = people.id
        self.answer_time_list = self.get_answer_time_list(people)
        self.article_time_list = self.get_article_time_list(people)
        self.comment_time_list = self.get_comment_time_list(people)
        self.favorite_column_list = self.get_favorite_column_list(people)
        self.favorite_topic_list = self.get_favorite_topic_list(people)
        self.question_time_list = self.get_question_time_list(people)
        self.favorite_user_id_list = self.get_favorite_user_id_list(people)
        self.follower_user_id_list = self.get_follower_user_id_list(people)
        self.live_time_list = self.get_live_time_list(people)
        self.thought_time_list = self.get_thought_time_list(people)

    def get_answer_time_list(self, people):
        time_set = set([answer.created_time for answer in people.answers])
        time_set.union([answer.updated_time for answer in people.answers])
        return list(time_set)

    def get_article_time_list(self, people):
        return [article.updated_time for article in people.articles]

    def get_comment_time_list(self, people):
        return []

    def get_favorite_column_list(self, people):
        return []

    def get_favorite_topic_list(self, people):
        return []

    def get_question_time_list(self, people):
        return []

    def get_favorite_user_id_list(self, people):
        return []

    def get_follower_user_id_list(self, people):
        return []

    def get_live_time_list(self, people):
        return []

    def get_thought_time_list(self, people):
        return []


