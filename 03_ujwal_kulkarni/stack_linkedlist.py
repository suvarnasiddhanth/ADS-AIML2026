class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, val):
        node = Node(val)
        if self.head:
            node.next = self.head
        self.head = node
        self.size += 1

    def pop(self):
        if self.isEmpty():
            print("Stack is empty!")
            return None

        popped_node = self.head
        self.head = self.head.next
        self.size -= 1
        return popped_node.data

    def peek(self):
        if self.isEmpty():
            print("Stack is empty!")
            return None
        return self.head.data

    def isEmpty(self):
        return self.size == 0

    def traverseAndPrint(self):
        if self.isEmpty():
            print("Stack is empty!")
            return

        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def stackSize(self):
        return self.size


# Menu-driven program
myStack = Stack()

while True:
    print("\n----- STACK MENU -----")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display Stack")
    print("5. Check if Stack is Empty")
    print("6. Stack Size")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        val = input("Enter value to push: ")
        myStack.push(val)
        print(val, "pushed onto the stack.")

    elif choice == '2':
        result = myStack.pop()
        if result is not None:
            print("Popped element:", result)

    elif choice == '3':
        result = myStack.peek()
        if result is not None:
            print("Top element:", result)

    elif choice == '4':
        print("Stack: ", end="")
        myStack.traverseAndPrint()

    elif choice == '5':
        print("Stack is empty:", myStack.isEmpty())

    elif choice == '6':
        print("Stack size:", myStack.stackSize())

    elif choice == '7':
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")
