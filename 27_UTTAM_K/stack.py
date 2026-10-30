"""
Stack using a Singly Linked List (LIFO = Last In, First Out)

Run on its own:     python stack.py
Or from main menu:  python main.py
"""


class Node:
    def __init__(self, data):
        self.data = data    # value stored
        self.next = None    # link to the node below


class Stack:
    def __init__(self):
        self.head = None    # head = TOP of the stack
        self.size = 0       # number of elements

    def is_empty(self):                 # O(1)
        return self.head is None

    def push(self, data):               # O(1)
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def pop(self):                      # O(1)
        if not self.head:
            return None
        value = self.head.data
        self.head = self.head.next
        self.size -= 1
        return value

    def peek(self):                     # O(1)
        return self.head.data if self.head else None

    def display(self):                  # O(n)
        if self.is_empty():
            print("Stack is empty.")
            return
        current = self.head
        print("TOP ->", end=" ")
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


# ---------------------------------------------------------------------
# Menu
# ---------------------------------------------------------------------
def read_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a whole number.")


my_stack = Stack()      # created once, so the data stays when you go back to the main menu


def menu():
    while True:
        print("\n------ STACK (Linked List) ------")
        print("1. Push")
        print("2. Pop")
        print("3. Peek (top element)")
        print("4. Display")
        print("5. Size")
        print("6. Is empty?")
        print("0. Back")
        choice = read_int("Enter choice: ")

        if choice == 1:
            value = read_int("Enter value to push: ")
            my_stack.push(value)
            print(value, "pushed.")
        elif choice == 2:
            if my_stack.is_empty():
                print("Stack underflow! The stack is empty.")
            else:
                print("Popped:", my_stack.pop())
        elif choice == 3:
            if my_stack.is_empty():
                print("Stack is empty.")
            else:
                print("Top element:", my_stack.peek())
        elif choice == 4:
            my_stack.display()
        elif choice == 5:
            print("Size:", my_stack.size)
        elif choice == 6:
            if my_stack.is_empty():
                print("Yes, the stack is empty.")
            else:
                print("No, the stack is not empty.")
        elif choice == 0:
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    menu()
