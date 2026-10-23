class Stack:
    def __init__(self):
        self.stack = []
    def push( self):
        ele=int(input("Enter the element to push: "))
        self.stack.append(ele)
        print("Element pushed to stack:", ele)
    def pop(self):
        if len(self.stack)==0:
            print("Stack is empty. Cannot pop element.")
        else:
            print("Element popped from stack:", self.stack.pop())
    def display(self):
        if len(self.stack)==0:
            print("Stack is empty.")
        else:
            print("Elements in stack:", self.stack[::-1])
    def peek(self):
        if len(self.stack)==0:
            print("Stack is empty. No top element.")
        else:
            print("Top element of stack:", self.stack[-1])
def main():
    stack = Stack()
    while True:
        print("\n Stack Operations Menu:")
        print("1. Push")
        print("2. Pop")
        print("3. Display")
        print("4. Peek")
        print("5. Exit")
        choice=int(input("Enter your choice (1-5):"))
        if choice==1:
            stack.push()
        elif choice==2:
            stack.pop()
        elif choice==3:
            stack.display()
        elif choice==4:
            stack.peek()
        elif choice==5:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__=="__main__":
    main()