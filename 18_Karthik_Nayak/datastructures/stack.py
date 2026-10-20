class stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def is_empty(self):
        return self.stack == []

    def pop(self):
        if self.is_empty():
            print("empty")
        else:
            return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return -1
        else:
            return self.stack[-1]

    def display(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print(self.stack)



def main():
    s = stack()

    while True:
        print("\n----- STACK MENU -----")
        print("1. Push (add item)")
        print("2. Pop (remove top item)")
        print("3. Peek (view top item)")
        print("4. Display stack")
        print("5. Check if empty")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            data = input("Enter item to push: ")
            s.push(data)
            print(f"{data} pushed onto the stack.")

        elif choice == "2":
            result = s.pop()
            if result is not None:
                print(f"Popped: {result}")

        elif choice == "3":
            result = s.peek()
            if result == -1:
                print("Stack is empty")
            else:
                print(f"Top item: {result}")

        elif choice == "4":
            print("Current stack:")
            s.display()

        elif choice == "5":
            print("Stack is empty." if s.is_empty() else "Stack is not empty.")

        elif choice == "6":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice! Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()