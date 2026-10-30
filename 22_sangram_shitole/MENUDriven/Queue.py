
# Queue Implementation using Linked List


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.count = 0

    # Enqueue operation
    # Adds an element at the rear
    def enqueue(self, data):
        new_node = Node(data)

        # If queue is empty
        if self.rear is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

        self.count += 1

    # Dequeue operation
    # Removes an element from the front
    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
            return None

        temp = self.front
        self.front = self.front.next

        # If queue becomes empty
        if self.front is None:
            self.rear = None

        self.count -= 1

        return temp.data

    # Get front element
    def peek(self):
        if self.front is None:
            print("Queue is empty")
            return None

        return self.front.data

    # Get rear element
    def rear_element(self):
        if self.rear is None:
            print("Queue is empty")
            return None

        return self.rear.data

    # Return size of queue
    def size(self):
        return self.count

    # Check if queue is empty
    def is_empty(self):
        return self.front is None

    # Display queue
    def display(self):
        if self.front is None:
            print("Queue is empty")
            return

        current = self.front

        print("Queue:", end=" ")

        while current is not None:
            print(current.data, end="")

            if current.next is not None:
                print(" <- ", end="")

            current = current.next

        print()
