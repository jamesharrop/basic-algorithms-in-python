# https://stackoverflow.com/questions/6103825/how-to-properly-use-unit-testings-assertraises-with-nonetype-objects

import unittest
from queue import Queue

class TestQueue(unittest.TestCase):
    """
    Tests for queue.py
    """

    def setUp(self):
        self.queue = Queue()

    def test_queue_with_one_item(self):
        self.queue.enqueue(1)
        out = self.queue.dequeue()
        self.assertTrue(out == 1)

    def test_queue_with_multiple_items(self):
        test_list = [1, 2, 3, 4, 5]
        for item in test_list:
            self.queue.enqueue(item)
        for item in test_list:
            self.assertTrue(self.queue.dequeue() == item)

    def test_queue_with_empty_queue(self):
        """ Check that an IndexError is raised by trying to remove an item from an empty queue """
        self.assertRaises(IndexError, lambda: self.queue.dequeue())

suite = unittest.TestLoader().loadTestsFromTestCase(TestQueue)
unittest.TextTestRunner(verbosity=2).run(suite)
