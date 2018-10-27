from helpers.config import read_configuration
from models.queue import Queue

print(read_configuration())

q = Queue('local')
print(q.queue_type)
q.put('asddsfdf')
print(q.size())
print(q.get())
print(q.size())