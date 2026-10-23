
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node

    def display(self):
        current = self.head

        if current is None:
            print("List is empty")
            return

        while current is not None:
            print(current.data, end=" -> ")
            current = current.next

        print("None")

    def update(self, old_value, new_value):
        current = self.head

        while current is not None:
            if current.data == old_value:
                current.data = new_value
                print("Node updated")
                return

            current = current.next

        print("Value not found")

    def delete(self, value):
        current = self.head

        if current is None:
            print("List is empty")
            return

        if current.data == value:
            self.head = current.next
            print("Node deleted")
            return

        while current.next is not None:
            if current.next.data == value:
                current.next = current.next.next
                print("Node deleted")
                return

            current = current.next

        print("Value not found")


def main():
    ll = LinkedList()

    while True:
        print("\n1. Insert")
        print("2. Display")
        print("3. Update")
        print("4. Delete")
        print("5. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            data = int(input("Enter data: "))
            ll.insert(data)

        elif choice == 2:
            ll.display()

        elif choice == 3:
            old_value = int(input("Enter value to update: "))
            new_value = int(input("Enter new value: "))
            ll.update(old_value, new_value)

        elif choice == 4:
            value = int(input("Enter value to delete: "))
            ll.delete(value)

        elif choice == 5:
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
 