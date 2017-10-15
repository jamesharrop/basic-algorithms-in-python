import unittest
from stack import Stack

class TestStack(unittest.TestCase):
    """
    Tests for stack.py
    """
    def setUp(self):
        self.stack = Stack()

    def test_stack_with_one_item(self):
        self.stack.push(1)
        out = self.stack.pop()
        self.assertTrue(out == 1)

    def test_stack_with_multiple_items(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        out = self.stack.pop()
        self.assertTrue(out == 3)
        out = self.stack.pop()
        self.assertTrue(out == 2)
        out = self.stack.pop()
        self.assertTrue(out == 1)

    def test_stack_with_empty_stack(self):
        out = self.stack.pop()

    def test_stack_peek(self):
        self.stack.push(1)
        self.assertTrue(self.stack.peek() == 1)
        # Then peek again to check the item is still on the stack
        self.assertTrue(self.stack.peek() == 1)

suite = unittest.TestLoader().loadTestsFromTestCase(TestStack)
unittest.TextTestRunner(verbosity=2).run(suite)