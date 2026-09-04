class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

#queue class
class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.count=0

    def enqueue(self,x) :
        node=Node(x)
        
    
        if self.isEmpty():
            self.front=self.rear=node
            self.count+=1
            print("element added succesfully")

        else:
            self.rear.next=node
            self.rear=node 
            self.count+=1
            print("element added succesfully")

    def dequeue(self):
        
        if self.isEmpty():
            print("queue is empty")  
            return None     
        else:
            temp=self.front.next
            removed_data=self.front.data
            print(self.front.data)   
            self.front=temp    
            self.count-=1
            print("element removed succesfully")
        # if queue  is empty     
        if self.front is None:
            self.rear = None
        return removed_data  

    def peek(self):
        if self.isEmpty():
            print("queue is empty")
            return None
        else:    
            return self.front.data  

    def size(self):
        return self.count     


    def isEmpty(self)   :
        if self.front==None:
            return True

        else:
            return False
             

    def isFull(self):
        pass

if __name__=="__main__":
    q = Queue()
    q.enqueue(6)
    q.enqueue(10)
    print("Dequeued:", q.dequeue())  
    print("Front element:", q.peek())  
    print("Size:", q.size())  





