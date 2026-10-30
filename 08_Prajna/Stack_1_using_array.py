class Stack:
    def __init__(self, capacity):
        self.stack = []
        self.capacity = capacity

    def push(self, element):
        if self.isFull():
            print("Stack Overflow")
        else:
            self.stack.append(element)
            print("Element pushed: ", element)

    def pop(self):
        if self.isEmpty():
            print("Stack Underflow")
        else:
            print("Popped element: ", self.stack.pop())

    def peek(self):
        if self.isEmpty():
            print("Stack Underflow")
        else:
            print("Top element: ", self.stack[-1])

    def display(self):
        if self.isEmpty():
            print("Stack Underflow")
        else:
            print("Stack(bottom to top): ", self.stack)

    def size(self):
        return len(self.stack)

    def search(self, element):
        for i in range(len(self.stack)):
            if self.stack[i] == element:
                print("Element found at index : ", i)
                return
        print("Element not found")

    def isEmpty(self):
        return len(self.stack) == 0

    def isFull(self):
        return len(self.stack) == self.capacity

def stack_array_menu():
    # create a stack
    capacity = int(input("Enter the capacity: "))
    myStack = Stack(capacity)

    while True:
        print("\n--- STACK USING ARRAY ---")
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
    stack_array_menu()
        