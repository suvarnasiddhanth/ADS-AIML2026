class Stack:

    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if len(self.stack) == 0:
            print('Stack Empty! Pop Not Possible!!')
            return

        return self.stack.pop()

    def peek(self):
        if not self.stack:
            print('Stack Empty! Peek Not Possible!!')
            return

        return self.stack[-1]

    def length(self):
        return len(self.stack)

    def display(self):
        if not self.stack:
            print('Stack Empty!')
            return

        print('Stack:', self.stack)


# Create stack
s = Stack()

s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)

print('Popped:', s.pop())
print('Top element:', s.peek())
print('Stack length:', s.length())
s.display()
