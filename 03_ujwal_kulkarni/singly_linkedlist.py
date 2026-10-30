class Node:
    def __init__(self,data):
        self.data = data
        self.next=None
class LinkedList:
    def __init__(self):
        self.front = None
        self.rear=None
        self.length = 0
    def insertBeginning(self, data):
        node = Node(data)
        if self.front is None:
            self.front=self.rear=node
        else:

            node.next=self.front
            self.front=node
        self.length+=1
    def insertEnd(self,data):
        node=Node(data)
        if self.rear is None:
            self.front=self.rea=node
        else:
            self.rear.next=node
            self.rear=node
        self.length+=1
    def insertPosition(self, data, pos):
        if pos<1 or pos>self.length+1:
            print("invalid")
            return
        if pos==1:
            self.insertBeginning(data)
            return
        if pos==self.length+1:
            self.insertEnd(data)
            return
        node=Node(data)
        temp=self.front
        for _ in range(pos-2):
            if temp.next is None:
                break
            temp=temp.next
        node.next=temp.next
        temp.next=node
        self.length+=1
    def del_front(self):
        if self.front is None:
            print("empty")
            return
        temp=self.front
        self.front=temp.next
        self.front-=1
    def del_rear(self):
        if self.front is None:
            print("empty")
            return
        if self.front==self.rear:
            print("Deletedd is", self.front.data)
            self.front=self.rear=None
        else:
            temp= self.front
            while temp.next!=self.rear:
                temp=temp.next
            print(self.rear.data)
            temp.next=None
            self.rear=temp
    def deleteValue(self, data):
        if self.front is None:
            print("List is empty")
            return

        temp = self.front
        prev = None
        while temp is not None:
            if temp.data == data:
                if prev is None:
                    self.front=temp.next
                else:

                    prev.next=temp.next
                if temp == self.rear:
                    self.rear =prev
                self.length-=1
                return
            prev = temp
            temp=temp.next
            
        



        
    

