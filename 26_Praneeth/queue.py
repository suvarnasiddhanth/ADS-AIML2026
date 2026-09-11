class queue:
    def __init__(self):
        self.queue=[]

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return 
        return self.queue.pop(0)

    
    def is_empty(self):
        return len(self.queue)==0

    def size(self):
        return len(self.queue)

    def peek(self):
        if self.is_empty():
            print("queue is empty")
        return self.queue[0]

    def display(self):
        if self.is_empty():
            print("The queue is empty")
            return
        print(self.queue)
        print("front is:", self.queue[0])
        print("rear is:", self.queue[-1])

q1=queue()

q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
q1.enqueue(40)

q1.display()

q1.dequeue()

q1.display()