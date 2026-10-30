
# Stack Implementation using Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.count = 0

    # Push operation
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.count += 1

    # Pop operation
    def pop(self):
        if self.top is None:
            print("Stack is empty")
            return None

        temp = self.top
        self.top = self.top.next
        self.count -= 1

        return temp.data

    # Peek operation
    def peek(self):
        if self.top is None:
            print("Stack is empty")
            return None

        return self.top.data

    # Size operation
    def size(self):
        return self.count

    # Check if stack is empty
    def is_empty(self):
        return self.top is None

    # Display stack
    def display(self):
        if self.top is None:
            print("Stack is empty")
            return

        current = self.top

        print("Stack:", end=" ")

        while current is not None:
            print(current.data, end=" ")
            current = current.next

        print()

