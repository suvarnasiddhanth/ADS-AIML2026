


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    # Insert at beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

        self.count += 1

    # Insert at end
    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.count += 1
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node
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

        new_node = Node(data)
        current = self.head

        for _ in range(position - 2):
            current = current.next

        new_node.next = current.next
        current.next = new_node

        self.count += 1

    # Delete from beginning
    def delete_at_beginning(self):
        if self.head is None:
            print("Linked List is empty")
            return None

        temp = self.head
        self.head = self.head.next

        self.count -= 1

        return temp.data

    # Delete from end
    def delete_at_end(self):
        if self.head is None:
            print("Linked List is empty")
            return None

        if self.head.next is None:
            data = self.head.data
            self.head = None
            self.count -= 1
            return data

        current = self.head

        while current.next.next is not None:
            current = current.next

        data = current.next.data
        current.next = None

        self.count -= 1

        return data

    # Delete from a specific position
    # Position starts from 1
    def delete_at_position(self, position):

        if self.head is None:
            print("Linked List is empty")
            return None

        if position < 1 or position > self.count:
            print("Invalid position")
            return None

        if position == 1:
            return self.delete_at_beginning()

        current = self.head

        for _ in range(position - 2):
            current = current.next

        temp = current.next
        current.next = temp.next

        self.count -= 1

        return temp.data

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

    # Display linked list
    def display(self):
        if self.head is None:
            print("Linked List is empty")
            return

        current = self.head

        print("Linked List:", end=" ")

        while current is not None:
            print(current.data, end="")

            if current.next is not None:
                print(" -> ", end="")

            current = current.next

        print()

    # Return size
    def size(self):
        return self.count

    # Check if empty
    def is_empty(self):
        return self.head is None