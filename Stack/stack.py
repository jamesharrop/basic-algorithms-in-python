class Stack(object):
    """
    Implementation of a stack in Python
    """

    def __init__(self):
        self.stack_store = []

    def push(self, new_item):
        self.stack_store.append(new_item)

    def pop(self):
        try:
            last_element = self.stack_store.pop()
            return last_element
        except IndexError:
            print("Error - pop() called - but no items in stack")

    def peek(self):
        try:
            return self.stack_store[-1]
        except IndexError:
            print("Error - peek() called - but no items in stack")
