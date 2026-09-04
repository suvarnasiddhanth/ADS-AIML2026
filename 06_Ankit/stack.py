class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.count = 0

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.count += 1

    def pop(self):
        if self.top is None:
            return None
        popped_val = self.top.data
        self.top = self.top.next
        self.count -= 1
        return popped_val

    def peek(self):
        if self.top is None:
            return None
        return self.top.data

    def len(self):
        return self.count


s = Stack()
s.push(10)
s.push(20)
s.push(30)

print(s.peek())
print(s.pop())
print(s.len())