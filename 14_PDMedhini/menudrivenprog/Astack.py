class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)
        print("Element pushed.")

    def pop(self):
        if len(self.items) == 0:
            print("Stack underflow! Stack is empty.")
        else:
            print("Popped element:", self.items.pop())

    def peek(self):
        if len(self.items) == 0:
            print("Stack is empty.")
        else:
            print("Top element:", self.items[-1])

    def display(self):
        if len(self.items) == 0:
            print("Stack is empty.")
        else:
            print("Stack (top to bottom):")
            for item in reversed(self.items):
                print(item)
