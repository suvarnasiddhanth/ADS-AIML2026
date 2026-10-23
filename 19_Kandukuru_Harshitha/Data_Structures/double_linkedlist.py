
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertion_at_beginning(self, data):
        newnode = Node(data)

        if self.head is None:
            self.head = self.tail = newnode
        else:
            newnode.next = self.head
            self.head.prev = newnode
            self.head = newnode

    def insertion_at_end(self, data):
        newnode = Node(data)

        if self.head is None:
            self.head = self.tail = newnode
        else:
            self.tail.next = newnode
            newnode.prev = self.tail
            self.tail = newnode

    def insertion_at_middle(self, data):
        if self.head is None:
            self.insertion_at_beginning(data)
            return

        slow = self.head
        fast = self.head

        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        newnode = Node(data)
        newnode.next = slow.next
        newnode.prev = slow

        if slow.next is not None:
            slow.next.prev = newnode
        else:
            self.tail = newnode

        slow.next = newnode

    def display(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head
        while temp is not None:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

    def display_reverse(self):
        if self.tail is None:
            print("List is empty")
            return

        temp = self.tail
        while temp is not None:
            print(temp.data, end=" <-> ")
            temp = temp.prev
        print("None")

    def delete_at_beginning(self):
        if self.head is None:
            print("List is empty")
            return

        self.head = self.head.next

        if self.head is None:
            self.tail = None
        else:
            self.head.prev = None

    def delete_at_end(self):
        if self.tail is None:
            print("List is empty")
            return

        self.tail = self.tail.prev

        if self.tail is None:
            self.head = None
        else:
            self.tail.next = None

    def delete_at_middle(self):
        if self.head is None:
            print("List is empty")
            return

        slow = self.head
        fast = self.head

        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        if slow.prev is None:
            self.delete_at_beginning()
        elif slow.next is None:
            self.delete_at_end()
        else:
            slow.prev.next = slow.next
            slow.next.prev = slow.prev

    def search(self, data):
        temp = self.head

        while temp is not None:
            if temp.data == data:
                print("Element found")
                return
            temp = temp.next

        print("Element not found")

    def insert_after(self, data, value):
        temp = self.head

        while temp is not None:
            if temp.data == value:
                newnode = Node(data)
                newnode.prev = temp
                newnode.next = temp.next

                if temp.next is not None:
                    temp.next.prev = newnode
                else:
                    self.tail = newnode

                temp.next = newnode
                return

            temp = temp.next

        print("Value not found")

    def insert_before(self, data, value):
        temp = self.head

        while temp is not None:
            if temp.data == value:
                newnode = Node(data)
                newnode.next = temp
                newnode.prev = temp.prev

                if temp.prev is not None:
                    temp.prev.next = newnode
                else:
                    self.head = newnode

                temp.prev = newnode
                return

            temp = temp.next

        print("Value not found")


def main():
    dll = DLL()

    while True:
        print("\n--- DOUBLY LINKED LIST MENU ---")
        print("1. Insert at beginning")
        print("2. Insert at end")
        print("3. Insert at middle")
        print("4. Display forward")
        print("5. Display reverse")
        print("6. Delete at beginning")
        print("7. Delete at end")
        print("8. Delete at middle")
        print("9. Search")
        print("10. Insert after a value")
        print("11. Insert before a value")
        print("12. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            data = int(input("Enter data: "))
            dll.insertion_at_beginning(data)

        elif choice == 2:
            data = int(input("Enter data: "))
            dll.insertion_at_end(data)

        elif choice == 3:
            data = int(input("Enter data: "))
            dll.insertion_at_middle(data)

        elif choice == 4:
            dll.display()

        elif choice == 5:
            dll.display_reverse()

        elif choice == 6:
            dll.delete_at_beginning()

        elif choice == 7:
            dll.delete_at_end()

        elif choice == 8:
            dll.delete_at_middle()

        elif choice == 9:
            data = int(input("Enter value to search: "))
            dll.search(data)

        elif choice == 10:
            value = int(input("Insert after which value? "))
            data = int(input("Enter new data: "))
            dll.insert_after(data, value)

        elif choice == 11:
            value = int(input("Insert before which value? "))
            data = int(input("Enter new data: "))
            dll.insert_before(data, value)

        elif choice == 12:
            print("Exiting program")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
