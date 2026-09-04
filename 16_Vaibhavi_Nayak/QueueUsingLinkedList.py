class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.count=0

    def isEmpty(self):
        return self.front is None

    def enqueue(self,data):
        newNode=Node(data)
        if self.isEmpty():
            self.front=self.rear=newNode
        else:
            self.rear.next=newNode
            self.rear=newNode
        self.count+=1

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        val=self.front.data
        self.front=self.front.next
        if self.front is None:
            self.rear=None

        self.count-=1
        return val

    def getFront(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        return self.front.data

    def size(self):
        return self.count


if __name__ == "__main__":
    q = Queue()
    
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(40)
    print("Dequeue :",q.dequeue())
    print("Queue size :",q.size())
    q.enqueue(30)
    print("Element at front :",q.getFront())
    print("Queue size :" ,q.size())



