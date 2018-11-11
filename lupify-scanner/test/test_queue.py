import unittest
import models.queue as queue

class TestConfiguration(unittest.TestCase):

    def setUp(self):
        self.conf = {'queue': 'local', 'targets': ['127.0.0.1', '192.168.1.1/32']}

    def test_queue_type_local(self):
        q = queue.Queue(self.conf)
        self.assertEqual('local', q.queue_type)

    def test_queue_type_invalid(self):
        self.assertRaises(ValueError, queue.Queue, {'queue': 'invalid_queue'})

    def test_queue_put(self):
        q = queue.Queue(self.conf)
        self.assertIsNone(q.put('item'))

    def test_queue_get(self):
        q = queue.Queue(self.conf)
        q.put('some_item')
        self.assertEqual('some_item', q.get())
        q.put('some_item_1')
        q.put('some_item_2')
        q.put('some_item_3')
        q.put('some_item_4')
        self.assertEqual('some_item_1', q.get())
        self.assertEqual('some_item_2', q.get())

    def test_queue_size(self):
        q = queue.Queue(self.conf)
        self.assertEqual(0, q.size())
        q.put('item')
        self.assertEqual(1, q.size())

    def test_queue_local_targets_missing(self):
        self.assertRaises(KeyError, queue.Queue, {'queue': 'local'})

    def test_queue_local_targets_wrong_type(self):
        self.assertRaises(TypeError, queue.Queue, {'queue': 'local', 'targets': 'hola'})

    def test_queue_local_initializing(self):
        q = queue.Queue(self.conf)
        self.assertEqual(False, q.initialize(['127.0.0.1']))


if __name__ == '__main__':
    unittest.main()
