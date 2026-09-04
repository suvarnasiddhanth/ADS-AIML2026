class stack:
    def __init__(self):
        self.stack=[]

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.is_empty():
            print("Stack Underflow")
            return None
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            print("No elements in stack")
            return None
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack)==0

    def size(self):
        return len(self.stack)

    def display(self):
        if self.is_empty():
            print("No elements in stack")
            return 

        print("Stack is:", self.stack)


s=stack()

s.push(9)
s.push(8)
s.push(2)
s.pop()
print(s.peek())
print(s.is_empty())
print(s.size())
s.display()