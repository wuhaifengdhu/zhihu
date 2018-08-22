import sys
import time

reload(sys)
sys.setdefaultencoding('UTF8')


class TaskQueue(object):
    def __init__(self, max_job_size, interval=10):
        self.max_job_size = max_job_size
        self.job_queue = list()
        self.interval = interval

    def add_job(self, job):
        while len(self.job_queue) == self.max_job_size:
            print("As current job is full, sleep %d seconds" % len(self.job_queue))
            time.sleep(self.interval)
            self.update_job_queue()
        print("Add new job into job process queue, current job queue size %d" % len(self.job_queue))
        self.job_queue.append(job)

    def update_job_queue(self):
        print("Start check job queue, before check size %d" % len(self.job_queue))
        self.job_queue = [job for job in self.job_queue if job.is_alive()]
        print("After check job queue, size %d" % len(self.job_queue))

    def is_finished(self):
        self.update_job_queue()
        return len(self.job_queue) == 0


taskQueue = TaskQueue(500)
