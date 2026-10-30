


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    # Insert at beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.count += 1

    # Insert at end
    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.count += 1

    # Insert at a specific position
    # Position starts from 1
    def insert_at_position(self, data, position):

        if position < 1 or position > self.count + 1:
            print("Invalid position")
            return

        if position == 1:
            self.insert_at_beginning(data)
            return

        if position == self.count + 1:
            self.insert_at_end(data)
            return

        new_node = Node(data)
        current = self.head

        for _ in range(position - 1):
            current = current.next

        new_node.prev = current.prev
        new_node.next = current

        current.prev.next = new_node
        current.prev = new_node

        self.count += 1

    # Delete from beginning
    def delete_at_beginning(self):
        if self.head is None:
            print("Doubly Linked List is empty")
            return None

        data = self.head.data

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

        self.count -= 1

        return data

    # Delete from end
    def delete_at_end(self):
        if self.tail is None:
            print("Doubly Linked List is empty")
            return None

        data = self.tail.data

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

        self.count -= 1

        return data

    # Delete from a specific position
    # Position starts from 1
    def delete_at_position(self, position):

        if self.head is None:
            print("Doubly Linked List is empty")
            return None

        if position < 1 or position > self.count:
            print("Invalid position")
            return None

        if position == 1:
            return self.delete_at_beginning()

        if position == self.count:
            return self.delete_at_end()

        current = self.head

        for _ in range(position - 1):
            current = current.next

        current.prev.next = current.next
        current.next.prev = current.prev

        self.count -= 1

        return current.data

    # Search for an element
    def search(self, data):
        current = self.head
        position = 1

        while current is not None:
            if current.data == data:
                return position

            current = current.next
            position += 1

        return -1

    # Display from head to tail
    def display_forward(self):
        if self.head is None:
            print("Doubly Linked List is empty")
            return

        current = self.head

        print("Forward:", end=" ")

        while current is not None:
            print(current.data, end="")

            if current.next is not None:
                print(" <-> ", end="")

            current = current.next

        print()

    # Display from tail to head
    def display_backward(self):
        if self.tail is None:
            print("Doubly Linked List is empty")
            return

        current = self.tail

        print("Backward:", end=" ")

        while current is not None:
            print(current.data, end="")

            if current.prev is not None:
                print(" <-> ", end="")

            current = current.prev

        print()

    # Return size
    def size(self):
        return self.count

    # Check if empty
    def is_empty(self):
        return self.head is None
