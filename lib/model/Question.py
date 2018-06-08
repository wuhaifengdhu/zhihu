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
        collect_people_set = set()
        for comment in comments:
            redisHelper.update_comments(comment.author.id, comment.created_time)
            if len(collect_people_set) < 10:
                collect_people_set.add(comment.author.id)
                break
        for user_id in collect_people_set:
            redisHelper.collect_crawl_people(user_id)
