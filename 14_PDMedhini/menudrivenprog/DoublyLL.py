
# doubly_linked_list.py

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head

            while temp.next is not None:
                temp = temp.next

            temp.next = new_node
            new_node.prev = temp

        print("Node inserted.")

    def delete(self, data):
        temp = self.head

        while temp is not None and temp.data != data:
            temp = temp.next

        if temp is None:
            print("Element not found.")
            return

        if temp.prev is not None:
            temp.prev.next = temp.next
        else:
            self.head = temp.next

        if temp.next is not None:
            temp.next.prev = temp.prev

        print("Node deleted.")

    def display(self):
        if self.head is None:
            print("List is empty.")
            return

        temp = self.head
        while temp is not None:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

    def display_reverse(self):
        if self.head is None:
            print("List is empty.")
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next

        while temp is not None:
            print(temp.data, end=" <-> ")
            temp = temp.prev
        print("None")
