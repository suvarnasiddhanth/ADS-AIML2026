class Node:
  def __init__ (self,data):
    self.data = data
    self.prev = None
    self.next = None

class DoublyLinkedList:
  def __init__(self):
    self.head = None

  def append(self,data):

    new_node = Node(data)

    if self.head is None:
      self.head = new_node
      return

    current = self.head
    while current.next:
      current = current.next

    current.next= new_node
    new_node.prev = current
    return

  def prepend (self,data):
    new_node = Node(data)
    new_node.next = self.head
    self.head.prev = new_node
    self.head = new_node
    return

  def display_forward(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

  def delete(self,value):
    current = self.head

    if current.data == value:
            self.head = current.next
            if self.head:
                self.head.prev = None
            return

    while current and current.data != value:
            current = current.nex

    if current is None:
            print(f"Value {value} not found.")
            return
    if current.prev:
            current.prev.next = current.next
    if current.next:
            current.next.prev = current.prev

dll = DoublyLinkedList()


dll.append(10)
dll.append(20)
dll.append(30)
dll.append(40)

dll.display_forward()
dll.prepend(67)
dll.display_forward()
