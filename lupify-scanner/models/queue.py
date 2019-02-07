import queue
import helpers.parsers as parsers

class QueueBase:
    def put(self, item):
        raise NotImplementedError

    def get(self):
        raise NotImplementedError

    def size(self):
        raise NotImplementedError

    def initialize(self, items):
        raise NotImplementedError

class Queue(QueueBase):
    def __init__(self, conf):
        self.queue_type = conf['queue']
        self._check_queue_type()
        self.queue = self._create_queue(conf)

    def _check_queue_type(self):
        if not self.queue_type in ['local']:
            raise ValueError

    def _create_queue(self, conf):
        if self.queue_type == 'local':
            if not 'targets' in conf:
                raise KeyError
            if not isinstance(conf['targets'], list):
                raise TypeError

            return LocalQueue()

    def initialize(self, items):
        if not isinstance(items, list):
            raise TypeError

        for item in parsers.target_list(items):
            self.put(item)
        return True

    def put(self, item):
        self.queue.put(item)

    def get(self):
        item = self.queue.get()
        self.put(item)
        return item

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

