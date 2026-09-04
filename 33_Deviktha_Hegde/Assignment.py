
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def display(self):
        current = self.head

        while current:
            print(current.data, end=" ")
            current = current.next

        print()

    def split(self):
        count = 0
        current = self.head

        while current:
            count += 1
            current = current.next

        
        middle = count // 2

        current = self.head

        for i in range(middle - 1):
            current = current.next
            

        stall1 = self.head
        stall2 = current.next
        current.next = None

        if stall2:
            stall2.prev = None

        return stall1, stall2


#  linked list
dll = DoublyLinkedList()

dll.insert_end("A")
dll.insert_end("B")
dll.insert_end("C")
dll.insert_end("D")
dll.insert_end("E")
dll.insert_end("F")

print("Original list:")
dll.display()

stall1, stall2 = dll.split()

print("Stall 1:")
current = stall1
while current:
    print(current.data, end=" ")
    current = current.next

print("\nStall 2:")
current = stall2
while current:
    print(current.data, end=" ")
    current = current.next