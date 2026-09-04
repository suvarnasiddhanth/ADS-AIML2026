class stack:
    def __init__(self):
        self.stack=[]
    
    def push(self,data):
        self.stack.append(data)
        

    def is_empty(self):
        return self.stack==[]

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
        print(self.stack)

s = stack()

s.push(10)
s.push(20)
s.push(30)

s.display()

print("Peek:", s.peek())
print("Pop:", s.pop())

s.display()

print("Pop:", s.pop())
print("Pop:", s.pop())

s.display()

s.pop()