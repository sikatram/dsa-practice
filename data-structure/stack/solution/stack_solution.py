class Stack:
    def __init__(self):
        # Initialize an empty list to hold stack items
        self.items = []

    def push(self, item):
        # Add an item to the top of the stack
        self.items.append(item)

    def pop(self):
        # Remove and return the top item from the stack, if not empty
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        # Return the top item from the stack without removing it, if not empty
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        # Check if the stack is empty
        return len(self.items) == 0

    def size(self):
        # Return the number of items in the stack
        return len(self.items)
