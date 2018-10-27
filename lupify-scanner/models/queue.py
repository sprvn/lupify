import queue

class QueueBase:
    def put(self, item):
        raise NotImplementedError

    def get(self):
        raise NotImplementedError

    def size(self):
        raise NotImplementedError

class Queue(QueueBase):
    def __init__(self, queue_type):
        self.queue_type = queue_type
        self.queue = self._create_queue()
        self._check_queue_type()

    def _check_queue_type(self):
        if not self.queue_type in ['local']:
            raise ValueError

    def _create_queue(self):
        if self.queue_type == 'local':
            return LocalQueue()

    def put(self, item):
        self.queue.put(item)

    def get(self):
        return self.queue.get()

    def size(self):
        return self.queue.size()


class LocalQueue(QueueBase):
    def __init__(self):
        self.queue = queue.Queue()

    def put(self, item):
        self.queue.put(item)

    def get(self):
        return self.queue.get()

    def size(self):
        return self.queue.qsize()

