class Node:
    def __init__(self, data):
        # Initialize a node with data and a reference to the next node
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        # Initialize an empty linked list with a head node
        self.head = None

    def display(self):
        # Display linked list elements
        current = self.head

        while current:
            print(current.data, end=" -> ")
            current = current.next

        print("None")

    def append(self, data):
        # Append new node with data to end of linked list
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node

    def prepend(self, data):
        # Prepend new node with data to beginning of linked list
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def remove(self, key):
        # Remove a node with the given key value from the linked list
        current = self.head

        if current and current.data == key:
            self.head = current.next
            return

        prev = None

        while current and current.data != key:
            prev = current
            current = current.next

        if current is None:
            return

        prev.next = current.next

    def reverse(self):
        # Reverse linked list in-place
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev
