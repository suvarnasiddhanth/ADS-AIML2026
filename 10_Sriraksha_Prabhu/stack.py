class stack:
    def __init__(self):
        self.stack=[]
    def push(self,data):
        self.stack.append(data)
    def pop(self):
        if self.IsEmpty():
            return "Stack is Empty"
        else:
            self.stack.pop()
    def peek(self):
        if self.IsEmpty():
            return "Stack is Empty"
        else:
            return self.stack[-1]
    def IsEmpty(self):
        return len(self.stack)==0
    def display(self):
        return self.stack
s=stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)

print("Elements are",s.display())
s.pop()
s.pop()
print("Elements after pop:",s.display())
print("Top Element is",s.peek())
print("Is stack Empty",s.IsEmpty())
print(s.peek())
