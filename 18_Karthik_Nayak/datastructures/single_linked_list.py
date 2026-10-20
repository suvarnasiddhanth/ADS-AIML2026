class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = new_node

    def traversal(self):
        current = self.head
        if current == None:
            print("List is empty.")
            return
        while current != None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # updation
    def update(self, old_data, new_data):
        current = self.head
        while current != None:
            if current.data == old_data:
                current.data = new_data
                print("Updated {old_data} to {new_data}.")
                return
            current = current.next
        print("{old_data} not found in the list.")

    # deletion
    def deletion(self, target):
        prev = None
        current = self.head
        while current != None:
            if current.data == target:
                if prev == None:
                    self.head = self.head.next
                else:
                    prev.next = current.next
                print("Deleted {target} from the list.")
                return
            prev = current
            current = current.next
        print("{target} not found in the list.")

    def insert_at_position(self, position, data):
        if position < 1:
            print("Invalid position ({position})! Position must be >= 1.")
            return

        new_node = Node(data)

        if position == 1:
            new_node.next = self.head
            self.head = new_node
            print("Inserted {data} at position {position}.")
            return

        current = self.head
        for i in range(position - 2):
            if current is None:
                print(f"Position {position} is out of range!")
                return
            current = current.next

        if current is None:
            print("Position {position} is out of range!")
            return

        new_node.next = current.next
        current.next = new_node
        print("Inserted {data} at position {position}.")



def main():
    my_list = LinkedList()

    while True:
        print("\n----- LINKED LIST MENU -----")
        print("1. Insert at end")
        print("2. Insert at position")
        print("3. Update a value")
        print("4. Delete a value")
        print("5. Traverse / Print list")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            data = input("Enter data to insert: ")
            my_list.insert(data)
            print("{data} inserted at the end.")

        elif choice == "2":
            try:
                position = int(input("Enter position: "))
            except ValueError:
                print("Position must be a number.")
                continue
            data = input("Enter data to insert: ")
            my_list.insert_at_position(position, data)

        elif choice == "3":
            old_data = input("Enter the value to update: ")
            new_data = input("Enter the new value: ")
            my_list.update(old_data, new_data)

        elif choice == "4":
            target = input("Enter the value to delete: ")
            my_list.deletion(target)

        elif choice == "5":
            print("Current list:")
            my_list.traversal()

        elif choice == "6":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice! Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()