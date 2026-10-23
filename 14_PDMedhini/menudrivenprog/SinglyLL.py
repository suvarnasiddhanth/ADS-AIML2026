
# singly_linked_list.py

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
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

        print("Node inserted.")

    def delete(self, data):
        if self.head is None:
            print("List is empty.")
            return

        if self.head.data == data:
            self.head = self.head.next
            print("Node deleted.")
            return

        temp = self.head
        while temp.next is not None:
            if temp.next.data == data:
                temp.next = temp.next.next
                print("Node deleted.")
                return
            temp = temp.next

        print("Element not found.")

    def display(self):
        if self.head is None:
            print("List is empty.")
            return

        temp = self.head
        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")
