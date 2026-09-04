class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

    def __repr__(self):
        return f"Node{self.data}"

class Doubly_linked_list:
    def __init__(self):
        self.head = None 

    def insert_at_begining(self, data):

        newNode = Node(data)

        if self.head is None :
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode

    def insert_at_middle(self,data, index):

        length = 0
        current = self.head

        while current:
            length += 1
            current = current.next

        if index < 0 or index > length:
            return "Index out of range"

    
        if index == 0:
            self.insert_at_begining(data)
            return
        
        for _ in range(index - 1):
            if current is None or current.next is None:
                break
            current = current.next

        if current is None:
            return "Index out of range"


        newNode = Node(data)

        newNode.next = current.next
        newNode.prev = current

        if current.next is not None:
            current.next.prev = newNode 
        else:
            self.tail = newNode
        current.next = newNode

    def insert_at_end(self, data):

        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode

    def delete_from_begining(self):
        if self.head is None:
            return "List is Empty"

        if self.head == self.tail:
            self.head = None
            self.tail = None
            return

        self.head = self.head.next
        self.head.prev = None

    def delete_from_middle(self, index):
        length = 0
        current = self.head
            
        while current:
            length += 1
            current = current.next
            
        if index < 0 or index >= length:
            return "Index out of range"
            
        if index == 0:
            self.delete_from_begining()
            return
        
        current = self.head
    
        for _ in range(index-1):
            if current is None or current.next is None:
                break
            current = current.next
            
        if current is None:
            return "Index out of range"
    
        node_to_delete = current.next
    
        if node_to_delete.next is None:
            self.delete_from_end()
            return
    
        current.next = node_to_delete.next
        node_to_delete.next.prev = current

    def delete_from_end(self):
        if self.head is None:
            return "List is Empty"

        if self.head == self.tail:
            self.head = None
            self.tail = None
            return

        self.tail = self.tail.prev
        self.tail.next = None

    def traverse(self,reverse = False):
            current = self.tail if reverse else self.head
            while current:
                print(current.data, "<->", end = " ")
                current = current.prev if reverse else current.next
            print("None")


if __name__ == '__main__':

    List = Doubly_linked_list()

print("Doubly Linked List Operations : ")

print("Current Linked List : ")
List.traverse()

print("Inserting at the begining : ")
List.insert_at_begining(50)
List.traverse()
print("Inserting at the begining : ")
List.insert_at_begining(40)
List.traverse()
print("Inserting at the begining : ")
List.insert_at_begining(30)
List.traverse()
print("Inserting at the begining : ")
List.insert_at_begining(20)
List.traverse()
print("Inserting at the begining : ")
List.insert_at_begining(10)
List.traverse()
print("\nReverse Traversal : ")
List.traverse(reverse = True)

print("\nInserting at the end : ")
List.insert_at_end(60)
List.traverse()

print("\nInserting between the nodes : ")
List.insert_at_middle(35, 2)
List.traverse()

print("\nDelete from the begining : ")
List.delete_from_begining()
List.traverse()

print("\nDelete from the end : ")
List.delete_from_end()
List.traverse()

print("\nDelete from the end : ")
List.delete_from_end()
List.traverse()

print("\nDelete from middle : ")
List.delete_from_middle(1)
List.traverse()