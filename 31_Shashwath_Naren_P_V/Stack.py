class Stack:
    def __init__(self):
        self.stack = []
        
    def push(self, element):
        self.stack.append(element)
    
    def pop(self):
        if self.isEmpty():
            return None
        return self.stack.pop()
    
    def peek(self):
        if self.isEmpty():
            return None
        return self.stack[-1]
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    
myStack = Stack()



m = "1"
while(m == "1"):
    
    print("1. Push\n2. Pop\n3. Peek\n4. IsEmpty\n5. Size\n6. Print Stack")
    choice = int(input("Enter your choice : "))
    
    match choice:
        case 1 :
            element = input("Enter an element to push into Stack : ")
            myStack.push(element)
        case 2 :
            if len(myStack.stack) == 0:
                print("Stack is Empty.")
            else:
                print("Popped Element from Stack : ", myStack.pop())
        case 3:
            if len(myStack.stack) == 0:
                            print("Stack is Empty.")
            else:
                print("Top element of Stack :  ", myStack.peek())
        case 4:
            print("Stack is Empty : ", myStack.isEmpty())
        case 5:
            print("Size of Stack : ", myStack.size())
        case 6 :
            print("Stack : ", myStack.stack)
        case _:
            print("Invalid Choice.")
    
    while True:    
        m = input("Do you want to continue operation(Yes = 1 / No = 0) : ")
        if m in ("1", "0"):
            break
        else:
            print("Wrong Choice! Please enter only 1 and 0.")

print("Program exited Sucessfully.")