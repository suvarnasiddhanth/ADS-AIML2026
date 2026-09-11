class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)

        if self.rear is None:
            self.front = self.rear = new_node
            return
        else: 
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
            return None

        data = self.front.data

        self.front = self.front.next

        if self.front is None:
            self.rear = None

        return data

    def peek(self):
        if self.front is None:
            print("Queue is empty")
            return None

        return self.front.data

    def display(self):
        if self.front is None:
            print("Queue is empty")
            return

        current = self.front

        while current:
            print(current.data, end=" ")
            current = current.next
            print()

q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.display()

print("Front element:", q.peek())

print("Deleted:", q.dequeue())

q.display()

