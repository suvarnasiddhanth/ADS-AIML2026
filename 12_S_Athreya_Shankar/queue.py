class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if len(self.queue) == 0:
            print('Queue Empty! Dequeue Not Possible!!')
            return

        return self.queue.pop(0)

    def peek(self):
        if not self.queue:
            print('Queue Empty! Peek Not Possible!!')
            return

        return self.queue[0]

    def length(self):
        return len(self.queue)

    def display(self):
        if not self.queue:
            print('Queue Empty!')
            return

        print('Queue:', self.queue)


q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)

print('Dequeued:', q.dequeue())
print('Front element:', q.peek())
print('Queue length:', q.length())
q.display()
