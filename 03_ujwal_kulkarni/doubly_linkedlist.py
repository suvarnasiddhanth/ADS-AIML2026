class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class LinkedList:
    def __init__(self):
        self.front=None
        self.rear = None
        self.length =0
    def insertfront(self,data):
        node=Node(data)
        if self.front is None:
            self.front=self.rear=node
        node.next=self.front
        self.front.prev=node
        self.front=node
        self.length+=1
    def insertEnd(self,data):
        node=Node(data)
        if self.rear is None:
            self.front=self.rear=node
        else:
                
            node.prev=self.rear
            self.rear.next=node
            self.rear=node
    def insertat(self, pos,data):
        if pos<1 or pos>self.length+1:
            raise ValueError('invalid number')
        node =Node(data)
        temp=self.front

        if pos==1:
            self.insertfront(data)
            return
        if pos==self.length-1:
            self.insertEnd(data)
            return
        for _ in range(pos-2):
            if temp.next is None:
                break
            temp=temp.next
        node.prev=temp
        node.next=temp.next
        temp.next.prev=node
        temp.next=node
        self.length+=1
    def del_front(self):
        if self.front is None:
            raise ValueError('empty')
        temp=self.front
        self.front=temp.next
        if self.front is None:
            self.rear=None
        else:
            self.front.prev=None
    def del_end(self):
        if self.rear is None:
            raise ValueError('empty')
        temp=self.rear
        self.rear=temp.prev
        if self.rear is None:
            self.front =None
        else:
            self.rear.next=None
    def del_at(self, data):
        temp = self.front
        while temp is not None:
            if temp.data==data:
                if temp.prev is None:
                    self.front=temp.next
                else:
                    temp.prev.next=temp.next
                if temp.next is None:
                    self.rear =temp.prev
                else:
                    temp.next.prev=temp.prev
            
                self.length-=1
            temp=temp.next


        

    