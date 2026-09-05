class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue.pop(0)
    
    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue[0]
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def display(self):
        print(self.queue)

q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()
print(q.dequeue())
q.display()
print(q.peek())
q.display()
print(q.is_empty())
print(q.dequeue())
print(q.dequeue())
print(q.is_empty())