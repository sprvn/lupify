from helpers.config import read_configuration
from models.queue import Queue
import helpers.parsers as helpers

print(read_configuration())

q = Queue(read_configuration())
print(q.queue_type)
q.put('asddsfdf')
print(q.size())
print(q.get())
print(q.size())

print(helpers.target_list(['172.17.0.0/23', '192.168.1.3', '192.168.4.0/25']))