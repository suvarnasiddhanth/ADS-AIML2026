class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Insert at beginning
    def insert_beginning(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = self.tail = new_node
            return

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    # Insert at end
    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = self.tail = new_node
            return

        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    # Display forward
    def display_forward(self):
        current = self.head

        while current:
            print(current.data, end=" <-> ")
            current = current.next

        print("None")

    # Display backward
    def display_backward(self):
        current = self.tail

        while current:
            print(current.data, end=" <-> ")
            current = current.prev

        print("None")

    # Delete from beginning
    def delete_beginning(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head == self.tail:
            self.head = self.tail = None
            return

        self.head = self.head.next
        self.head.prev = None

    # Delete from end
    def delete_end(self):
        if self.tail is None:
            print("List is empty")
            return

        if self.head == self.tail:
            self.head = self.tail = None
            return

        self.tail = self.tail.prev
        self.tail.next = None

    # Search
    def search(self, data):
        current = self.head

        while current:
            if current.data == data:
                return True
            current = current.next

        return False

    # Length
    def length(self):
        count = 0
        current = self.head

        while current:
            count += 1
            current = current.next

        return count

    # Reverse
    def reverse(self):
        current = self.head

        while current:
            current.next, current.prev = current.prev, current.next
            current = current.prev

        self.head, self.tail = self.tail, self.head
        
        
dll = DoublyLinkedList()

dll.insert_end(10)
dll.insert_end(20)
dll.insert_end(30)

dll.display_forward()