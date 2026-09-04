
class Stack:
    def __init__(self):
        self.stack= []
        
    
    def push(self,data):
        self.stack.append(data)
        
    def pop(self):
        if len(self.stack)==0:
            print('Stack empty')
        else:
            return self.stack.pop()
        
    def peek(self):
        if len(self.stack)==0:
            print('Stack empty')
        else:
            return self.stack[-1]
        
    def is_empty(self):
        return len(self.stack) == 0


s=Stack()
s.push(90)
s.push(80)
s.push(70)

print(s.peek())

s.pop()
print(s.peek())

print(s.is_empty())

s.pop()
s.pop()
print(s.is_empty())