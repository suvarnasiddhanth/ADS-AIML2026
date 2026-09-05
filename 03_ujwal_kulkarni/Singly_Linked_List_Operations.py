class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __repr__(self):
        return f"Node({self.data})"
    
    
class Singly_Linked_List:
    def __init__(self):
        self.head = None
        
    def insert_at_begining(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
        
    def insert_at_end(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = newNode
    
    def insert_at_index(self, data, index):
        
        length = 0
        current = self.head
        while current:
            length += 1
            current = current.next
            
        if index < 0 or index > length:
            print("Index out of range")
            return
        
        if index == 0:
            self.insert_at_begining(data)
            return

        current = self.head
            # Traverse until we reach the node right before our target index
        for _ in range(index - 1):
            if current is None or current.next is None:
                 break
            current = current.next

        if current is None:
            return "Index out of range"

        newNode = Node(data)
        newNode.next = current.next
        current.next = newNode

        
    def delete_from_begining(self):
        if self.head is None:
            return "The List is empty"
        self.head = self.head.next
    
    def delete_from_end(self):
        if self.head is None:
            return "The List is empty"
        if self.head.next is None:
            self.head = None
            return
        
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None


    def delete_from_index(self, index):
        length = 0
        current = self.head

        while current:
            length += 1
            current = current.next

        if index < 0 or index >= length:
            print("Index out of range")
            return

        if index == 0:
            self.delete_from_begining
            return

        current = self.head
        for _ in range(index - 1):
            current = current.next

        current.next = current.next.next

        
    def search(self, value):
        current = self.head
        position = 0
        while current:
            if current.data == value:
                return f"Value : '{value}' found at the position '{position}'"
            current = current.next
            position += 1
        return f"Value {value} not found in the list"
        
    def traverse(self):
        current = self.head
        while current: 
            print(current.data, " <->", end = " ")
            current = current.next   
        print("None")
    
    
if __name__ == '__main__':
    
    List = Singly_Linked_List()

print("Linked List Operations : ")
print("\nCurrent Linked List :")
List.traverse()
print("\nInserting at the begining of a node : ")    
List.insert_at_begining(10)
List.traverse()
List.insert_at_begining(20)
List.traverse()
List.insert_at_begining(30)
List.traverse()
List.insert_at_begining(40)
List.traverse()
List.insert_at_begining(50)



List.traverse()  
print("\nInserting at the end : ")
List.insert_at_end(60)
List.traverse()

print("\nSearching through linked list : ")
print(list.search(20),"\n")

print("Deleting from the begining : ")
List.delete_from_begining()
List.traverse()

print("\nSearching through linked list : ")
print(List.search(50), "\n")

print("\nDeleting from the end : ")
List.delete_from_end()
List.traverse()

print("\nSearching through linked list : ")
print(List.search(30), "\n")

print("Deleting from the : ")
List.delete_from_end()
List.traverse()

print("\nSearching through linked list : ")
print(List.search(10), "\n")

print("\nInsert at index : ")

List.insert_at_index(455, 0)

List.traverse()
List.insert_at_index(90, 2)

List.traverse()

List.insert_at_index(452, 5)

List.traverse()

List.insert_at_index(55, 10)

List.traverse()

print("\nDelete from index : ")
List.delete_from_index(3)
List.traverse()

List.delete_from_index(9)