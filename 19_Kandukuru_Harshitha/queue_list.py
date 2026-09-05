class Queue_list:
    def __init__(self):
        self.queue = []
    def enqueue(self,item):
        self.queue.append(item)
        print("Enqueued element:", item)
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty, nothing to dequeue()")
        else:
            a = self.queue.pop(0)
            print("Dequeued element:", a)
    def is_empty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False
    def display(self):
        print("Queue elements:", self.queue)
    def front_display(self):
        if self.is_empty():
            print("Queue is empty, no front element")
        else:
            print("Front element:", self.queue[0])
    def rear_display(self):
        if self.is_empty():
            print("Queue is empty, no rear element")
        else:
            print("Rear element:", self.queue[-1])
    def size(self):
        print("Size of the queue:", len(self.queue))

q=Queue_list()
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)    
q.front_display()
q.rear_display()
q.display()
q.size()
q.dequeue()
q.dequeue()
q.display()
print(q.is_empty())