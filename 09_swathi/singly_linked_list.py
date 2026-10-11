
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.n = 0

    def insert_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.n += 1

    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

        self.n += 1

    def insert_at_position(self, data, position):
        if position < 0 or position > self.n:
            print("Invalid position!")
            return

        if position == 0:
            self.insert_front(data)
            return

        new_node = Node(data)
        current = self.head

        for _ in range(position - 1):
            current = current.next

        new_node.next = current.next
        current.next = new_node
        self.n += 1

    def delete_front(self):
        if self.head is None:
            print("List is empty!")
            return

        self.head = self.head.next
        self.n -= 1

    def delete_end(self):
        if self.head is None:
            print("List is empty!")
            return

        if self.head.next is None:
            self.head = None
        else:
            current = self.head
            while current.next.next:
                current = current.next
            current.next = None

        self.n -= 1

    def delete_at_position(self, position):
        if position < 0 or position >= self.n:
            print("Invalid position!")
            return

        if position == 0:
            self.delete_front()
            return

        current = self.head
        for _ in range(position - 1):
            current = current.next

        current.next = current.next.next
        self.n -= 1

    def search(self, data):
        current = self.head
        position = 0

        while current:
            if current.data == data:
                print(f"Element found at position {position}")
                return

            current = current.next
            position += 1

        print("Element not found!")

    def reverse(self):
        previous = None
        current = self.head

        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        self.head = previous

    def display(self):
        if self.head is None:
            print("List is empty!")
            return

        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def length(self):
        print("Length:", self.n)


def singly_linked_list_menu():
    linked_list = SinglyLinkedList()

    while True:
        print("\n--- SINGLY LINKED LIST ---")
        print("1. Insert at front")
        print("2. Insert at end")
        print("3. Insert at position")
        print("4. Delete at front")
        print("5. Delete at end")
        print("6. Delete at position")
        print("7. Search")
        print("8. Reverse")
        print("9. Display")
        print("10. Length")
        print("11. Back to main menu")

        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                data = int(input("Enter data: "))
                linked_list.insert_front(data)

            elif choice == "2":
                data = int(input("Enter data: "))
                linked_list.insert_end(data)

            elif choice == "3":
                data = int(input("Enter data: "))
                position = int(input("Enter position (0-based): "))
                linked_list.insert_at_position(data, position)

            elif choice == "4":
                linked_list.delete_front()

            elif choice == "5":
                linked_list.delete_end()

            elif choice == "6":
                position = int(input("Enter position (0-based): "))
                linked_list.delete_at_position(position)

            elif choice == "7":
                data = int(input("Enter element to search: "))
                linked_list.search(data)

            elif choice == "8":
                linked_list.reverse()
                print("List reversed.")

            elif choice == "9":
                linked_list.display()

            elif choice == "10":
                linked_list.length()

            elif choice == "11":
                break

            else:
                print("Invalid choice!")

        except ValueError:
            print("Please enter a valid integer.")
