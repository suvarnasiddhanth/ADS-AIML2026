
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self):
        value = int(input("Enter value: "))
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node

        print(value, "inserted")

    def delete(self):
        if self.head is None:
            print("List is empty")
            return

        value = int(input("Enter value to delete: "))

        if self.head.data == value:
            self.head = self.head.next
            print(value, "deleted")
            return

        temp = self.head
        while temp.next is not None:
            if temp.next.data == value:
                temp.next = temp.next.next
                print(value, "deleted")
                return
            temp = temp.next

        print("Value not found")

    def search(self):
        value = int(input("Enter value to search: "))
        temp = self.head

        while temp is not None:
            if temp.data == value:
                print("Value found")
                return
            temp = temp.next

        print("Value not found")

    def display(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head
        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


s = SinglyLinkedList()

while True:
    print("\n--- Singly Linked List Menu ---")
    print("1. Insert")
    print("2. Delete")
    print("3. Search")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        s.insert()
    elif choice == 2:
        s.delete()
    elif choice == 3:
        s.search()
    elif choice == 4:
        s.display()
    elif choice == 5:
        print("Exiting...")
        break
    else:
        print("Invalid choice")
