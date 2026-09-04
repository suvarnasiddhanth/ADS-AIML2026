#double linked list
class Node:
  def __init__(self, data):
    self.data = data
    self.prev = None
    self.next = None

class DoublyLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

#Forward Display
def display_fwd(self):
  if self.head is None:
    print('List is empty')
    return
  cur = self.head
  while cur is not None:
    print(cur.data)
    cur=cur.next

  print('None')


#Backward Display
def display_back(self):
  if self.head is None:
    print('List is empty')
    return
  cur=self.tail
  while cur is not None:
    print(cur.data)
    cur=cur.prev

  print('None')

#Insert at beginning
def insert_beginning(self, data):
  newnode=Node(data)

  if self.head is None:
    self.head = newnode
    self.tail = newnode
  else:
    newnode.next = self.head
    self.head.prev = newnode
    self.head = newnode


#Insert at the End
def insert_end(self,data):
  newnode=Node(data)
  if self.head is None:
    self.head=newnode
    self.tail=newnode
  else:
    self.tail.next=newnode
    newnode.prev=self.tail
    self.tail=newnode


#Insert at position
def insert_position(self,data,position):
  newnode=Node(data)

  if position == 0:
    self.insert_beginning(data)
    return



    cur=self.head