class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
class LinkedList:
    def __init__(self):
        self.head=None
    def insert_front(self, data):
        node=Node(data,self.head)
        self.head=node

    def insert_end(self, data):
        if self.head is None:
            self.head=Node(data,None)
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data,None)
    def len(self):
        count =0
        itr=self.head
        while itr:
            count=count+1
            itr=itr.next
        return count
    def insert_at(self,data,index):
        if index<0 or index> self.len():
            print('invalid index')
        if index==0:
            self.insert_front(data)
        itr = self.head
        count =0
        while itr:
            if count==index-1:
                node =Node(data, itr.next)
                itr.next=node
            itr=itr.next
            count+=1
    def insert_values(self, data):
        for i in data:
            self.insert_end(i)
            
    def delete_front(self):
        if self.head is None:
            print("empty List")
        self.head=self.head.next

    def delete_end(self):
        if self.head is None:
            print("empty List")
        if self.head.next is None:
            self.head=None
        itr=self.head
        while itr.next.next:
            itr=itr.next
        itr.next=None
    def delete_at(self,index):
        if index<0 or index> self.len():
            print('invalid index')
        if index==0:
            self.head=self.head.next
        itr = self.head
        count =0
        while itr:
            if count==index-1:
                itr.next=itr.next.next
            itr=itr.next
            count+=1
    
    def search(self,val):
        itr=self.head
        count=0
        while itr:
            if itr.data==val:
                print(f'{val} is at {count+1}')
            itr=itr.next
            count+=1
    def print_list(self):
        if self.head is None:
            print("empty list")
            return
        itr =self.head
        res=[]
        while itr:
            res.append(itr.data)
            itr=itr.next
        print(res)


l1=LinkedList()
l1.insert_front(4)
l1.insert_front(5)
l1.insert_front(6)
l1.insert_end(3)
l1.insert_end(2)
l1.insert_values([-1,-2,-3])
l1.print_list()
print('Length of the List:',l1.len())
l1.delete_front()
print('delete front')
l1.print_list()
print('delete end')
l1.delete_end()
l1.print_list()
print('Length of the List:',l1.len())
l1.insert_at(15,4)
print('Length of the List:',l1.len())
l1.print_list()
print("delete at->\n")
l1.delete_at(4)
l1.print_list()
print('Length of the List:',l1.len())
l1.search(15)
#doubly linked liset
class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_front(self, data):
        node = Node(data, next=self.head, prev=None)
        if self.head is not None:
            self.head.prev = node
        self.head = node
        if self.tail is None:
            self.tail = node

    def insert_end(self, data):
        if self.head is None:
            self.insert_front(data)
            return
        node = Node(data, next=None, prev=self.tail)
        self.tail.next = node
        self.tail = node

    def lent(self):
        count = 0
        itr = self.head
        while itr:
            itr = itr.next
            count += 1
        return count

    def insert_at(self, data, index):
        if index < 0 or index > self.lent():
            print("invalid index")
            return
        if index == 0:
            self.insert_front(data)
            return
        if index == self.lent():
            self.insert_end(data)
            return

        itr = self.head
        count = 0
        while count < index - 1:
            itr = itr.next
            count += 1
        node = Node(data, next=itr.next, prev=itr)
        itr.next.prev = node
        itr.next = node

    def del_front(self):
        if self.head is None:
            print('empty')
            return
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        else:
            self.tail = None

    def del_end(self):
        if self.tail is None:
            print('empty')
            return
        self.tail = self.tail.prev
        if self.tail is not None:
            self.tail.next = None
        else:
            self.head = None

    def del_at(self, index):
        if self.head is None:
            print('empty')
            return
        if index < 0 or index >= self.lent():
            print("invalid index")
            return
        if index == 0:
            self.del_front()
            return
        if index == self.lent() - 1:
            self.del_end()
            return

        itr = self.head
        count = 0
        while count < index:
            itr = itr.next
            count += 1
        itr.prev.next = itr.next
        itr.next.prev = itr.prev

    def print_list(self):
        if self.head is None:
            print('empty')
            return
        itr = self.head
        res = []
        while itr:
            res.append(itr.data)
            itr = itr.next
        print(res)

    def print_reverse(self):
        if self.tail is None:
            print('empty')
            return
        itr = self.tail
        res = []
        while itr:
            res.append(itr.data)
            itr = itr.prev
        print(res)


l1 = DoublyLinkedList()
l1.insert_front(20)
l1.insert_front(10)
l1.insert_end(30)
l1.insert_end(40)
l1.print_list()
l1.print_reverse()
l1.insert_at(25, 2)
l1.print_list()
l1.del_at(0)
l1.print_list()
l1.del_end()
l1.print_list()
