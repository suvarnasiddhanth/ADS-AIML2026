class Stack:
    def __init__(self):
        self.stack = []

    def push(self):
        value = int(input("Enter value: "))
        self.stack.append(value)
        print(value, "pushed into stack")

    def pop(self):
        if len(self.stack) == 0:
            print("Stack Underflow")
        else:
            print("Popped element:", self.stack.pop())

    def peek(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:
            print("Top element:", self.stack[-1])

    def display(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:
            print("Stack elements:", self.stack[::-1])

s = Stack()

while True:
    print("\n1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        s.push()
    elif choice == 2:
        s.pop()
    elif choice == 3:
        s.peek()
    elif choice == 4:
        s.display()
    elif choice == 5:
        print("Exiting...")
        break
    else:
        print("Invalid choice")