from apscheduler.schedulers.blocking import BlockingScheduler
from rq import Queue
from worker import conn
from email_processor import forward_emails

sched = BlockingScheduler()
q = Queue(connection=conn)


@sched.scheduled_job('interval', minutes=5)
def timed_job():
    result = q.enqueue(forward_emails)
    print('This job is run every three minutes.')

sched.start()
