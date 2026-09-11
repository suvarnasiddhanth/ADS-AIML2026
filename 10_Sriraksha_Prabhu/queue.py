class queue:
    def __init__(self):
        self.queue=[]
    def enque(self,data):
        self.queue.append(data)
    def dequeue(self):
        if queue==self.IsEmpty():
            return "Queue is Empty"
        else:
            return self.queue.pop(0)
    def IsEmpty(self):
        return len(self.queue)==0
    def size(self):
        if queue==self.IsEmpty():
            return "Queue is Empty"
        else:
            return len(self.queue)
    def frontElement(self):
        if queue==self.IsEmpty():
            return "Queue is Empty"
        else:
            return self.queue[0]
    def rear(self):
         if queue==self.IsEmpty():
            return "Queue is Empty"
         else:
            return self.queue[-1]
    def display(self):
        return self.queue

q=queue()
q.enque(10)
q.enque(20)
q.enque(30)
q.enque(40)
print(q.display())
q.dequeue()
print(q.display())
print(q.IsEmpty())
print(q.size())
print(q.frontElement())
print(q.rear())
