"""
Doubly Linked List (every node links forward AND backward)

Positions start at 1 (1 = first node).

Run on its own:     python doubly_linked_list.py
Or from main menu:  python main.py
"""


class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None    # link backward
        self.next = None    # link forward


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Insert at front                         Time O(1)
    def insert_front(self, data):
        new_node = DNode(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        else:
            self.tail = new_node    # empty list: new node is also the tail
        self.head = new_node

    # Insert at end                           Time O(1)
    def insert_tail(self, data):
        new_node = DNode(data)
        if not self.tail:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    # Insert at a position (1 = first)        Time O(n)
    def insert_at_position(self, pos, data):
        n = self.length()
        if pos < 1 or pos > n + 1:
            return False                # invalid position
        if pos == 1:
            self.insert_front(data)
        elif pos == n + 1:
            self.insert_tail(data)
        else:
            current = self.head
            for _ in range(pos - 1):    # walk to the node currently AT this position
                current = current.next
            new_node = DNode(data)
            new_node.prev = current.prev    # new node points both ways first
            new_node.next = current
            current.prev.next = new_node    # then the neighbours point to it
            current.prev = new_node
        return True

    # Delete at front                         Time O(1)
    def delete_head(self):
        if not self.head:
            return None
        value = self.head.data
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        return value

    # Delete at end                           Time O(1)  (prev link: no walking needed)
    def delete_tail(self):
        if not self.tail:
            return None
        value = self.tail.data
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        return value

    # Delete the first node with this value   Time O(n)
    def delete_value(self, value):
        current = self.head
        while current and current.data != value:
            current = current.next
        if current is None:
            return False                        # not found
        if current.prev:
            current.prev.next = current.next    # left neighbour skips over current
        else:
            self.head = current.next            # deleting the head
        if current.next:
            current.next.prev = current.prev    # right neighbour skips back over current
        else:
            self.tail = current.prev            # deleting the tail
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

    # Display head -> tail (follows next)     Time O(n)
    def display_forward(self):
        current = self.head
        print("None <->", end=" ")
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    # Display tail -> head (follows prev)     Time O(n)
    def display_backward(self):
        current = self.tail
        print("None <->", end=" ")
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")


# ---------------------------------------------------------------------
# Menu
# ---------------------------------------------------------------------
def read_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a whole number.")


my_dlist = DoublyLinkedList()   # created once, so the data stays when you go back to the main menu


def menu():
    while True:
        print("\n------ DOUBLY LINKED LIST ------")
        print("1. Insert at beginning")
        print("2. Insert at end")
        print("3. Insert at position")
        print("4. Delete from beginning")
        print("5. Delete from end")
        print("6. Delete a value")
        print("7. Search")
        print("8. Display forward")
        print("9. Display backward")
        print("10. Count nodes")
        print("0. Back")
        choice = read_int("Enter choice: ")

        if choice == 1:
            value = read_int("Enter value: ")
            my_dlist.insert_front(value)
            print(value, "inserted at the beginning.")
        elif choice == 2:
            value = read_int("Enter value: ")
            my_dlist.insert_tail(value)
            print(value, "inserted at the end.")
        elif choice == 3:
            value = read_int("Enter value: ")
            pos = read_int("Enter position (1 = first): ")
            if my_dlist.insert_at_position(pos, value):
                print(value, "inserted at position", pos)
            else:
                print("Invalid position. Valid range is 1 to", my_dlist.length() + 1)
        elif choice == 4:
            value = my_dlist.delete_head()
            if value is None:
                print("List is empty. Nothing to delete.")
            else:
                print("Deleted:", value)
        elif choice == 5:
            value = my_dlist.delete_tail()
            if value is None:
                print("List is empty. Nothing to delete.")
            else:
                print("Deleted:", value)
        elif choice == 6:
            value = read_int("Enter value to delete: ")
            if my_dlist.delete_value(value):
                print(value, "deleted.")
            else:
                print(value, "not found in the list.")
        elif choice == 7:
            value = read_int("Enter value to search: ")
            pos = my_dlist.search(value)
            if pos == -1:
                print(value, "not found.")
            else:
                print(value, "found at position", pos)
        elif choice == 8:
            if my_dlist.head is None:
                print("List is empty.")
            else:
                my_dlist.display_forward()
        elif choice == 9:
            if my_dlist.tail is None:
                print("List is empty.")
            else:
                my_dlist.display_backward()
        elif choice == 10:
            print("Number of nodes:", my_dlist.length())
        elif choice == 0:
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    menu()
