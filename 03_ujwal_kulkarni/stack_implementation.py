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
s=stack()
s.push(1)
s.push(2)
s.push(3)


print("Stack: ", s.stack)
print("Pop: ", s.pop())
print("Stack after Pop: ", s.stack)
print("Peek: ", s.peek())
print("isEmpty: ", s.isEmpty())
print("Size: ", s.size())