
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
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
            new_node.prev = temp

        print(value, "inserted")

    def delete(self):
        if self.head is None:
            print("List is empty")
            return

        value = int(input("Enter value to delete: "))
        temp = self.head

        while temp is not None and temp.data != value:
            temp = temp.next

        if temp is None:
            print("Value not found")
            return

        if temp.prev is not None:
            temp.prev.next = temp.next
        else:
            self.head = temp.next

        if temp.next is not None:
            temp.next.prev = temp.prev

        print(value, "deleted")

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
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")


d = DoublyLinkedList()

while True:
    print("\n--- Doubly Linked List Menu ---")
    print("1. Insert")
    print("2. Delete")
    print("3. Search")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        d.insert()
    elif choice == 2:
        d.delete()
    elif choice == 3:
        d.search()
    elif choice == 4:
        d.display()
    elif choice == 5:
        print("Exiting...")
        break
    else:
        print("Invalid choice")
