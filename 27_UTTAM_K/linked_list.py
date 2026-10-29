"""
Singly Linked List

Positions start at 1 (1 = first node).

Run on its own:     python linked_list.py
Or from main menu:  python main.py
"""


class Node:
    def __init__(self, data):
        self.data = data    # the value stored
        self.next = None    # link to the next node (None = no next)


class LinkedList:
    def __init__(self):
        self.head = None    # first node
        self.tail = None    # last node

    # Insert at head                          Time O(1)
    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        if self.tail is None:       # list was empty, new node is also the tail
            self.tail = new_node

    # Insert at tail (with tail pointer)      Time O(1)
    def insert_at_tail(self, data):
        new_node = Node(data)
        if not self.head:           # empty list
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node   # link old last node to new node
            self.tail = new_node        # move tail forward

    # Insert at a position (1 = first)        Time O(n)
    def insert_at_position(self, pos, data):
        n = self.length()
        if pos < 1 or pos > n + 1:
            return False                # invalid position
        if pos == 1:
            self.insert_at_head(data)
        elif pos == n + 1:
            self.insert_at_tail(data)
        else:
            current = self.head
            for _ in range(pos - 2):    # stop at the node BEFORE the position
                current = current.next
            new_node = Node(data)
            new_node.next = current.next    # link first...
            current.next = new_node         # ...then attach
        return True

    # Delete at head                          Time O(1)
    def delete_at_head(self):
        if not self.head:
            return None
        value = self.head.data
        self.head = self.head.next
        if not self.head:           # list is now empty
            self.tail = None
        return value

    # Delete at tail                          Time O(n)
    def delete_at_tail(self):
        if not self.head:
            return None
        if self.head is self.tail:  # only one node
            value = self.head.data
            self.head = self.tail = None
            return value
        current = self.head
        while current.next is not self.tail:    # find node before tail
            current = current.next
        value = self.tail.data
        current.next = None
        self.tail = current
        return value

    # Delete the first node with this value   Time O(n)
    def delete_value(self, value):
        prev = None
        current = self.head
        while current and current.data != value:
            prev = current
            current = current.next
        if current is None:
            return False                # not found
        if prev is None:
            self.head = current.next    # deleting the head
        else:
            prev.next = current.next    # skip over current
        if current is self.tail:
            self.tail = prev            # deleting the tail
        return True

    # Search: returns position (1 = first) or -1   Time O(n)
    def search(self, value):
        current = self.head
        pos = 1
        while current:
            if current.data == value:
                return pos
            current = current.next
            pos += 1
        return -1

    # Count the nodes                         Time O(n)
    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    # Traverse / display                      Time O(n)
    def display(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print('None')


# ---------------------------------------------------------------------
# Menu
# ---------------------------------------------------------------------
def read_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a whole number.")


my_list = LinkedList()      # created once, so the data stays when you go back to the main menu


def menu():
    while True:
        print("\n------ SINGLY LINKED LIST ------")
        print("1. Insert at beginning")
        print("2. Insert at end")
        print("3. Insert at position")
        print("4. Delete from beginning")
        print("5. Delete from end")
        print("6. Delete a value")
        print("7. Search")
        print("8. Display")
        print("9. Count nodes")
        print("0. Back")
        choice = read_int("Enter choice: ")

        if choice == 1:
            value = read_int("Enter value: ")
            my_list.insert_at_head(value)
            print(value, "inserted at the beginning.")
        elif choice == 2:
            value = read_int("Enter value: ")
            my_list.insert_at_tail(value)
            print(value, "inserted at the end.")
        elif choice == 3:
            value = read_int("Enter value: ")
            pos = read_int("Enter position (1 = first): ")
            if my_list.insert_at_position(pos, value):
                print(value, "inserted at position", pos)
            else:
                print("Invalid position. Valid range is 1 to", my_list.length() + 1)
        elif choice == 4:
            value = my_list.delete_at_head()
            if value is None:
                print("List is empty. Nothing to delete.")
            else:
                print("Deleted:", value)
        elif choice == 5:
            value = my_list.delete_at_tail()
            if value is None:
                print("List is empty. Nothing to delete.")
            else:
                print("Deleted:", value)
        elif choice == 6:
            value = read_int("Enter value to delete: ")
            if my_list.delete_value(value):
                print(value, "deleted.")
            else:
                print(value, "not found in the list.")
        elif choice == 7:
            value = read_int("Enter value to search: ")
            pos = my_list.search(value)
            if pos == -1:
                print(value, "not found.")
            else:
                print(value, "found at position", pos)
        elif choice == 8:
            if my_list.head is None:
                print("List is empty.")
            else:
                my_list.display()
        elif choice == 9:
            print("Number of nodes:", my_list.length())
        elif choice == 0:
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    menu()
