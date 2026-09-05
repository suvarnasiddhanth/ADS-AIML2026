class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    def insert_position(self, data, position):
        if position < 1:
            print("Invalid position")
            return

        if position == 1:
            self.insert_beginning(data)
            return

        new_node = Node(data)
        temp = self.head

        for _ in range(position - 2):
            if temp is None:
                print("Position out of range")
                return
            temp = temp.next

        if temp is None:
            print("Position out of range")
            return

        new_node.next = temp.next
        temp.next = new_node

    def delete_beginning(self):
        if self.head is None:
            print("List is empty")
            return

        self.head = self.head.next

    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next is None:
            self.head = None
            return

        temp = self.head
        while temp.next.next:
            temp = temp.next

        temp.next = None

    def delete_position(self, position):
        if self.head is None:
            print("List is empty")
            return

        if position < 1:
            print("Invalid position")
            return

        if position == 1:
            self.delete_beginning()
            return

        temp = self.head

        for _ in range(position - 2):
            if temp is None or temp.next is None:
                print("Position out of range")
                return
            temp = temp.next

        if temp.next is None:
            print("Position out of range")
            return

        temp.next = temp.next.next

    def search(self, key):
        temp = self.head
        position = 1

        while temp:
            if temp.data == key:
                print(f"{key} found at position {position}")
                return position

            temp = temp.next
            position += 1

        print(f"{key} not found")
        return -1

    def display(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")

    def length(self):
        count = 0
        temp = self.head

        while temp:
            count += 1
            temp = temp.next

        return count

    def update(self, position, data):
        if position < 1:
            print("Invalid position")
            return

        temp = self.head

        for _ in range(position - 1):
            if temp is None:
                print("Position out of range")
                return
            temp = temp.next

        if temp is None:
            print("Position out of range")
            return

        temp.data = data

    def reverse(self):
        previous = None
        current = self.head

        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        self.head = previous

    def find_middle(self):
        if self.head is None:
            print("List is empty")
            return

        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        print("Middle element:", slow.data)
        return slow.data

    def contains(self, key):
        temp = self.head

        while temp:
            if temp.data == key:
                return True
            temp = temp.next

        return False

    def clear(self):
        self.head = None


ll = SinglyLinkedList()
ll.insert_beginning(10)
ll.insert_beginning(5)
ll.insert_end(20)
ll.insert_end(30)
ll.insert_position(15, 3)
print("Linked List:")
ll.display()
ll.search(20)
print("Length:", ll.length())
ll.update(2, 100)
print("After update:")
ll.display()
ll.delete_beginning()
print("After deleting beginning:")
ll.display()
ll.delete_end()
print("After deleting end:")
ll.display()
ll.delete_position(2)
print("After deleting position 2:")
ll.display()
ll.find_middle()
ll.reverse()
print("After reversing:")
ll.display()
print("Contains 15:", ll.contains(15))
ll.clear()
print("After clearing:")
ll.display()
