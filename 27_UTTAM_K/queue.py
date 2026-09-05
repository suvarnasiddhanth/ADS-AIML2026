from collections import deque
#queue

class Queue:
    def __init__(self):
        self.items = deque()

    def is_empty(self):
        
        return len(self.items) == 0

    def enqueue(self, item):
        
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.items.popleft()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self.items[0]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(list(self.items))


print_queue = Queue()


print_queue.enqueue("Am I Dreaming")
print_queue.enqueue("Make it to the morning")
print_queue.enqueue("The color violet")

print(f"Current queue: {print_queue}")
print(f"Next in queue: {print_queue.peek()}") 


printed_doc = print_queue.dequeue()
print(f"Successfully printed: {printed_doc}")
print(f"Remaining in queue: {print_queue.size()}")