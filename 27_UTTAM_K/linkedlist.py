#singly linked list

class Node:
  def __init__ (self,data):
    self.data = data
    self.next = None

class single:
  def __init__(self):
      self.head = None
  def insert_attail(self,data):
      new_node = Node(data)
      if not self.head :
        self.head = new_node
        return
      current = self.head
      while current.next:
        current = current.next
      current.next = new_node

  def insert_athead(self,data):
      new_node = Node(data)
      new_node.next = self.head
      self.head = new_node

  def delete(self, key):
      current = self.head

      if current and current.data == key:
          self.head = current.next
          current = None
          return

      prev = None
      while current and current.data != key:
          prev = current
          current = current.next
      if current is None:
          return
      prev.next = current.next
      current = None

  def search(self, key):
    current = self.head
    while current:
      if current.data == key:
        return True
      current = current.next
    return False

  def display(self):
    elements= []
    current = self.head
    while current:
      elements.append(current.data)
      current = current.next
    print(elements)


if __name__ == "__main__":
  singlelist = single()
  singlelist.insert_attail(1)
  singlelist.insert_attail(2)
  singlelist.insert_attail(3)
  singlelist.insert_athead(4)
  singlelist.display()
  singlelist.delete(2)
  singlelist.display()
  print(singlelist.search(4))