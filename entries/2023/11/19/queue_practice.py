class Queue:
    def __init__(self):
        # Initialize an empty list to hold queue items
        self.items = []

    def enqueue(self, item):
        # Add an item to the back of the queue
        self.items.append(item)

    def dequeue(self):
        # Remove and return the front item from the queue, if not empty
        if not self.is_empty():
            return self.items.pop(0)

    def front(self):
        # Return front item without removal, if not empty
        if not self.is_empty():
            return self.items[0]

    def is_empty(self):
        # Check if the queue is empty
        return self.size() == 0

    def size(self):
        # Return the number of items in the queue
        return len(self.items)
