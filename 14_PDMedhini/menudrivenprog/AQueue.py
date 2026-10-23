class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, data):
        self.items.append(data)
        print("Element inserted into queue.")

    def dequeue(self):
        if len(self.items) == 0:
            print("Queue underflow! Queue is empty.")
        else:
            print("Deleted element:", self.items.pop(0))

    def front(self):
        if len(self.items) == 0:
            print("Queue is empty.")
        else:
            print("Front element:", self.items[0])

    def display(self):
        if len(self.items) == 0:
            print("Queue is empty.")
        else:
            print("Front ->", self.items, "<- Rear")
