class Deque:
    def __init__(self):
        self.items = []

    def add_front(self, item):
        self.items.insert(0, item)

    def add_rear(self, item):
        self.items.append(item)

    def remove_front(self):
        if self.is_empty():
            return "Deque is empty"
        return self.items.pop(0)

    def remove_rear(self):
        if self.is_empty():
            return "Deque is empty"
        return self.items.pop()

    def peek_front(self):
        if self.is_empty():
            return "Deque is empty"
        return self.items[0]

    def peek_rear(self):
        if self.is_empty():
            return "Deque is empty"
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

d = Deque()

d.add_rear(10)
d.add_rear(20)
d.add_front(5)

print("Deque:", d.items)
print("Front:", d.peek_front())
print("Rear:", d.peek_rear())

print("Removed from front:", d.remove_front())
print("Removed from rear:", d.remove_rear())

print("Deque after deletion:", d.items)
print("Size:", d.size())
