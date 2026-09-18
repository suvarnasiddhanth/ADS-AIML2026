class stack:
    def __init__(self):
        self.stack = []
# push operation
    def push(self,element):
        self.stack.append(element)               # add the element to the top of the stack
        print(element,"pushed into the stack")

# pop operation
    def pop(self):
        if len(self.stack) == 0:
            print("stack overflow")
        else :
            element = self.stack.pop()
            print(element,"popped from the stack ")

# peek operation
    def peek(self):
        if len(self.stack) == 0:
            print("stack overflow")
        else :
            print("Top element is ", self.stack[-1])    # display the top element without removing it

# display operation
    def display(self):
        if len(self.stack) == 0:
            print("stack overflow")
        else :
             print("Display :", self.stack)

# is empty operation
    def is_empty(self):
        if len(self.stack) == 0:
            print("stack overflow")
        else :
            print("stack is not empty")

s = stack()
s.push(10)
s.push(20)
s.push(30)
s.pop()
s.peek()
s.display()
s.is_empty()
                






