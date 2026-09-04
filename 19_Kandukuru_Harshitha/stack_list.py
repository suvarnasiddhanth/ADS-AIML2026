class Stack:
    def __init__(self):
        self.stack=[]
    def push(self,item):
        self.stack.append(item)
        print("pushed element:",item)
    def pop(self):
        if self.IS_Empty():
            print("Stack is empty ntg to pop()")
        else:
            a=self.stack.pop()
            print("poped element:",a)
    def display(self):
        print("Stack elements:", self.stack)
    def top_display(self):
        print("Top element:", self.stack[0])
    def IS_Empty(self):
        if len(self.stack)==0:
            print("Stack is empty")
        else:
            print("Stack is not empty")
s=Stack()
s.push(3)
s.push(4)
s.push(5)
s.push(6)
s.pop()
s.display()
s.push(8)
s.top_display()
s.display()
s.IS_Empty()