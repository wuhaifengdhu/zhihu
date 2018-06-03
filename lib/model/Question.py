import sys
from lib.db.RedisHelper import redisHelper

reload(sys)
sys.setdefaultencoding('UTF8')


class Question(object):
    @staticmethod
    def handle(question):
        print("handle question id: %d" % question.id)
        if not redisHelper.is_question_exist(question.id):
            Question.handle_comments(question.comments)
            for answer in question.answers:
                Question.handle_comments(answer.comments)
        else:
            print("Exist")

    @staticmethod
    def handle_answer(answer):
        Question.handle_comments(answer.comments)

    @staticmethod
    def handle_comments(comments):
        for comment in comments:
            redisHelper.update_comments(comment.author.id, comment.created_time)
            redisHelper.collect_crawl_people(comment.author.id)
