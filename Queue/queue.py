# http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html
# https://stackoverflow.com/questions/4426663/how-do-i-remove-the-first-item-from-a-python-list

class Queue(object):
    """
    Implementation of a queue in Python
    A FIFO (first in, first out data structure)

    Example usage:

    >>> queue = Queue()
    >>> queue.enqueue(1)
    >>> queue.enqueue(2)
    >>> print(queue.dequeue())
    2

    """

    def __init__(self):
        self.queue_store = []

    def enqueue(self, new_item):
        """ Add a new item to the back of the queue """
        self.queue_store.append(new_item)

    def dequeue(self):
        """ Remove an item from the front of the queue """
        return self.queue_store.pop(0)