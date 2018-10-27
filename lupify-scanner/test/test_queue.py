import unittest
import models.queue as queue

class TestConfiguration(unittest.TestCase):

    def setUp(self):
        pass

    def test_queue_type_local(self):
        self.assertEqual('local', queue.Queue('local').queue_type)

    def test_queue_type_invalid(self):
        self.assertRaises(ValueError, queue.Queue, 'invalid_type')

    def test_queue_put(self):
        q = queue.Queue('local')
        self.assertIsNone(q.put('item'))

    def test_queue_get(self):
        q = queue.Queue('local')
        q.put('some_item')
        self.assertEqual('some_item', q.get())
        q.put('some_item_1')
        q.put('some_item_2')
        q.put('some_item_3')
        q.put('some_item_4')
        self.assertEqual('some_item_1', q.get())
        self.assertEqual('some_item_2', q.get())

    def test_queue_size(self):
        q = queue.Queue('local')
        self.assertEqual(0, q.size())
        q.put('item')
        self.assertEqual(1, q.size())


if __name__ == '__main__':
    unittest.main()
