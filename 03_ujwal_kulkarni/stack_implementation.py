class stack:
    def __init__(self):
        self.stack=[]
    def push(self,data):
        self.stack.append(data)
    def pop(self):
        if self.size()==0:
            print("Stack is empty")
            return
        return self.stack.pop()
    def peek(self):
        if self.size()==0:
            print("Stack is empty")
            return
        return self.stack[-1]
    def size(self):
        return len(self.stack)
    def isEmpty(self):
        return len(self.stack) == 0
myStack = Stack()

m = "1"

while(m == "1"):
    print("\n1. Push\n2. Pop\n3. Peek\n4. IsEmpty\n5. Size\n6. Print Stack")
    choice = int(input("Enter your choice : "))

    match choice:

        case 1:
            element = int(input("Enter an element to insert into Stack : "))
            myStack.push(element)

        case 2:
            if len(myStack.stack) == 0:
                print("Stack is Empty.")
            else:
                print("Deleted element from Stack : ", myStack.pop())

        case 3:
            if len(myStack.stack) == 0:
                print("Stack is Empty.")
            else:
                print("Peek element of Stack : ", myStack.peek())

        case 4:
            print("Stack is Empty : ", myStack.isEmpty())

        case 5:
            print("Size of Stack : ", myStack.size())

        case 6:
            print("Stack : ", myStack.stack)

        case _:
            print("Invalid choice.")

    while True:
        m = input("Do you want to continue operation (Yes = 1 / No = 0) : ")

        if m in ("1", "0"):
            break
        else:
            print("Wrong Choice, Please enter only 1 and 0.")

print("Program exited Successfully.")
