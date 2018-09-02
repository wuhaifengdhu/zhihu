# -*- coding:utf-8 -*-
import sys
from lib.model.SetQueue import waiting_crawl_queue

reload(sys)
sys.setdefaultencoding('UTF8')


class Question(object):
    @staticmethod
    def handle(question, sqlite_helper):
        print("handle question id: %d" % question.id)
        if not sqlite_helper.is_question_exist(question.id):
            Question.handle_comments(question.comments, sqlite_helper)
            for answer in question.answers:
                Question.handle_comments(answer.comments, sqlite_helper)
        else:
            print("Question id %d exist, avoid duplicate effort" % question.id)

    @staticmethod
    def handle_answer(answer, sqlite_helper):
        Question.handle_comments(answer.comments, sqlite_helper)

    @staticmethod
    def handle_comments(comments, sqlite_helper):
        for comment in comments:
            sqlite_helper.update_comments(comment.author.id, comment.created_time)
            if comment.author.id is not None:
                waiting_crawl_queue.add(comment.author.id)
