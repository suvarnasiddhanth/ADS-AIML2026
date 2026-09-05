class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class Stack:
    def __init__(self):
        self.top=None

    def push(self, data):
        new_node=Node(data)
        if self.top is None:
            self.top=new_node
            return
        new_node.next=self.top
        self.top=new_node

    def pop(self):
        if self.top is None:
            print("Stack is Underflow")
            return None
        data=self.top.data
        self.top=self.top.next
        return data

    def peek(self):
        if self.top is None:
            print("No elements in stack")
            return
        return self.top.data

    def size(self):
        temp=self.top
        len=0
        while temp:
            len+=1
            temp=temp.next
        return len

    def display(self):
        temp=self.top
        while temp:
            print(temp.data, end="->")
            temp=temp.next
        print("None")

s=Stack()
s.push(10)
s.push(20)
s.push(30)
print(s.pop())
print("top of the stack:",s.peek())
print(f"the stack is:{s.display()}")
print("size of stack:",s.size())

