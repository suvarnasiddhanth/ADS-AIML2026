class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class Queue:
    def __init__(self):
        self.front=None
        self.rear=None

    def enqueue(self, data):
        new_node=Node(data)
        if self.rear is None:
            self.front=new_node
            self.rear=new_node
            return
        self.rear.next=new_node
        self.rear=new_node

    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
            return
        self.front=self.front.next

    def display(self):
        if self.front is None:
            print("queue is empty")
            return 

        temp=self.front
        while temp:
            print(temp.data, end="<-")
            temp=temp.next
        print("none")

        print("front is:", self.front.data)
        print("rear is:", self.rear.data)
        

q1=Queue()
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)

q1.display()
q1.dequeue()
q1.display()
q1.dequeue()
q1.dequeue()
q1.display()
