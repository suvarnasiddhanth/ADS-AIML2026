class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Singly Linked List class
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at beginning
    def insert_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert at end
    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node

    # Insert at a specific position
    def insert_at_position(self, data, position):
        if position == 0:
            self.insert_beginning(data)
            return

        new_node = Node(data)
        current = self.head

        for i in range(position - 1):
            if current is None:
                print("Position out of range")
                return
            current = current.next

        if current is None:
            print("Position out of range")
            return

        new_node.next = current.next
        current.next = new_node

    # Insert after a given value
    def insert_after_value(self, target, data):
        current = self.head

        while current is not None:
            if current.data == target:
                new_node = Node(data)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next

        print("Value not found")

    # Delete from beginning
    def delete_beginning(self):
        if self.head is None:
            print("List is empty")
            return

        self.head = self.head.next

    # Delete from end
    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next is None:
            self.head = None
            return

        current = self.head

        while current.next.next is not None:
            current = current.next

        current.next = None

    # Delete at a specific position
    def delete_at_position(self, position):
        if self.head is None:
            print("List is empty")
            return

        if position == 0:
            self.head = self.head.next
            return

        current = self.head

        for i in range(position - 1):
            if current is None or current.next is None:
                print("Position out of range")
                return
            current = current.next

        if current.next is None:
            print("Position out of range")
            return

        current.next = current.next.next

    # Delete by value
    def delete_by_value(self, data):
        if self.head is None:
            print("List is empty")
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head

        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

        print("Value not found")

    # Search for a value
    def search(self, data):
        current = self.head
        position = 0

        while current is not None:
            if current.data == data:
                return position
            current = current.next
            position += 1

        return -1

    # Update a value
    def update(self, old_data, new_data):
        current = self.head

        while current is not None:
            if current.data == old_data:
                current.data = new_data
                return
            current = current.next

        print("Value not found")

    # Count nodes
    def count_nodes(self):
        count = 0
        current = self.head

        while current is not None:
            count += 1
            current = current.next

        return count

    # Reverse the linked list
    def reverse(self):
        previous = None
        current = self.head

        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        self.head = previous

    # Find middle node
    def find_middle(self):
        if self.head is None:
            return None

        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow.data

    # Display
    def display(self):
        if self.head is None:
            print("List is empty")
            return

        current = self.head

        while current is not None:
            print(current.data, end=" -> ")
            current = current.next

        print("None")


