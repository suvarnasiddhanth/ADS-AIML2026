
class Stack:
    def __init__(self,max):
        self.stack = []
        self.max=max
    def is_empty(self):
        return  len(self.stack)==0
    def push(self, data):
        if len(self.stack) == self.max:
            print("overflow")
            return
        self.stack.append(data)
        print(data, " Inserted")
    def pop(self):
        if self.is_empty():
            raise IndexError('Pop from empty stack')
        return self.stack.pop()
    def peek(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.stack[-1]
    def print_stack(self):
        if self.is_empty():
            raise IndexError("Empty stack")
        return self.stack[::-1]
s1=Stack(5)
print("1.push")
print("2.pop")
print("3.peek")
print("4.display")
print("5.exit")
while True:

    choice=int(input("Enter the choice\n"))
    if choice==1:
        data=int(input("Enter the element to be inserted"))
        s1.push(data)
    if choice==2:
        s1.pop()
    if choice==3:
        s1.peek()
    if choice==4:
        print(s1.print_stack())
    if choice ==5:
        break


