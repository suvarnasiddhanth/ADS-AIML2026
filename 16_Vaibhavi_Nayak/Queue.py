class Queue:
    def __init__(self):
        self.q=[]

    def enqueue(self,x):
        self.q.append(x)

    def dequeue(self):
        return self.q.pop(0)

    

    def isEmpty(self):
        return len(self.q)==0

    def getFront(self):
            if self.isEmpty():
                 print("Queue empty")
                 return 
            return self.q[0]

    def size(self):
        return len(self.q)


if __name__ =="__main__":

    q=Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    print("Initial queue:", q.q)
    print("Is queue Empty ? " , q.isEmpty())
    print("Peek :",q.getFront())
    print("Elements dequeued:")
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print("Is queue Empty ? " , q.isEmpty())
    print("Peek  :",q.getFront())
