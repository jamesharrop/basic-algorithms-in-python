from stack import Stack

def main():
    """
    Example Stack() usage
    """
    stack = Stack()
    stack.push("apple")
    stack.push("pear")
    stack.push("banana")
    print(stack.peek())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())

if __name__ == "__main__":
    main()