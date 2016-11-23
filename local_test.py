from rq import Queue
from worker import conn
from email_processor import forward_emails

q = Queue(connection=conn)

q.enqueue(forward_emails)    
