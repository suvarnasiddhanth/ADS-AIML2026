
class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)
        print(f"{data} pushed onto the stack.")

    def pop(self):
        if self.is_empty():
            print("Stack is empty! Cannot pop.")
            return

        print("Popped element:", self.items.pop())

    def peek(self):
        if self.is_empty():
            print("Stack is empty!")
            return

        print("Top element:", self.items[-1])

    def display(self):
        if self.is_empty():
            print("Stack is empty!")
            return

        print("Stack (top to bottom):")
        for item in reversed(self.items):
            print(item)

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        print("Stack size:", len(self.items))


def stack_menu():
    stack = Stack()

    while True:
        print("\n--- STACK MENU ---")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Display")
        print("5. Check if empty")
        print("6. Size")
        print("7. Back to main menu")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            try:
                data = int(input("Enter data: "))
                stack.push(data)
            except ValueError:
                print("Please enter a valid integer.")

        elif choice == "2":
            stack.pop()

        elif choice == "3":
            stack.peek()

        elif choice == "4":
            stack.display()

        elif choice == "5":
            print("Stack is empty." if stack.is_empty()
                  else "Stack is not empty.")

        elif choice == "6":
            stack.size()

        elif choice == "7":
            break

        else:
            print("Invalid choice!")
