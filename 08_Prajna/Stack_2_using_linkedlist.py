class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack():
    def __init__(self):
        self.top = None
        self.count = 0

    def push(self, element):
        new_node = Node(element)
        new_node.next = self.top
        self.top = new_node
        self.count += 1
        print("Element pushed: ", element)

    def pop(self):
        if self.isEmpty():
            print("Stack Underflow")
        else:
            print("Popped Element: ", self.top.data)
            self.top = self.top.next
            self.count -= 1

    def peek(self):
        if self.isEmpty():
            print("Stack Underflow")
        else:
            print("Top element: ", self.top.data)

    def display(self):
        if self.isEmpty():
            print("Stack Underflow")
            return
        current = self.top
        print("Stack (top to bottom): ", end= " ")
        while current:
            print(current.data, end= " -> ")
            current = current.next
        print("None")

    def size(self):
        return self.count

    def search(self, element):
        current = self.top
        index = 0
        while current:
            if current.data == element:
                print("Element found at index: ", index)
                return
            current = current.next
            index += 1
        print("Element not found")

    def isEmpty(self):
        return self.top is None

 # Linked-list stack has no fixed capacity
    def isFull(self):
        return False

def stack_linked_list_menu():
    myStack = Stack()

    while True:
        print("\n--- STACK USING LINKED LIST ---")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Display")
        print("5. Size")
        print("6. Search")
        print("7. isEmpty")
        print("8. isFull")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            element = input("Enter element to push: ")
            myStack.push(element)

        elif choice == "2":
            myStack.pop()

        elif choice == "3":
            myStack.peek()

        elif choice == "4":
            myStack.display()

        elif choice == "5":
            print("Stack size:", myStack.size())

        elif choice == "6":
            element = input("Enter element to search: ")
            myStack.search(element)

        elif choice == "7":
            print("Stack is empty:", myStack.isEmpty())

        elif choice == "8":
            print("Stack is full:", myStack.isFull())

        elif choice == "9":
            print("Exiting program")
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    stack_linked_list_menu()