class Node:
    def __init__(self, data, next=None, prev=None):
        self.data=data
        self.next=next
        self.prev=prev

class LinkedList():
    def __init__(self):
        self.head=None
        self.tail=None
        
    def insert_front(self, data):
        node= Node(data, next=self.head, prev=None)

        if self.head is not None:
            self.head.prev= node
        self.head=node
        if self.tail is None:
            self.tail=node
    def insert_end(self,data):
        if self.head is None:
            self.head=Node(data, next=None,prev=None)
            self.tail=self.head
            return
        node = Node(data, next=None, prev=self.tail)
        self.tail.next=node
        self.tail=node
    def size(self):
        if self.head is None:
            return 0
        itr=self.head
        count=0
        while itr:
            itr=itr.next
            count +=1
        return count
    def insert_at(self, data, index):
        if index<0 or index> self.size():
            print("Invalid index")
            return
        if index==0:
            self.insert_front(data)
            return
        if index==self.size():
            self.insert_end(data)
            return
        itr=self.head
        count=0
        while count< index-1:
            itr=itr.next
            count +=1
        node=Node(data, next=itr.next, prev=itr)
        itr.next.prev=node
        itr.next=node
    def del_front(self):
        if self.head is None:
            print("Empty List")
            return
        self.head=self.head.next
        if self.head is not None:
            self.head.prev=None
        else:
            self.tail= None
    def del_end(self):
        if self.head is None:
            print("Empty List")
            return
        self.tail=self.tail.prev
        if self.tail is not None:
            self.tail.next= None
        else:
            self.head=None
    def del_at(self, index):
        if index <0 or index>= self.size():
            print("Invalid Index")
            return
        if index==0:
            self.del_front()
            return
        if index==self.size()-1:
            self.del_end()
            return
        count=0
        itr = self.head
        while count< index:
            itr=itr.next
            count +=1
        itr.prev.next=itr.next
        itr.next.prev=itr.prev
        
    def print_list(self, rev=None):
        if self.head is None:
            print('Empty')
            return
        if rev==False:
            itr=self.head
            res=[]
            while itr:
                res.append(itr.data)
                itr= itr.next
            print(res)
        else:
            itr=self.tail
            res=[]
            while itr:
                res.append(itr.data)
                itr=itr.prev
            print(res)
            
    
    
    

l1 = LinkedList()
l1.insert_front(20)
l1.insert_front(10)
l1.insert_end(30)
l1.insert_end(40)
print("Size :",l1.size())
l1.print_list()
l1.print_list(False)
l1.insert_at(25, 2)
l1.print_list()
l1.del_at(0)
l1.print_list()
print("Size :",l1.size())
l1.del_end()
l1.print_list(False)
l1.print_list(True)