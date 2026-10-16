class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self):
        value = int(input("Enter value: "))
        self.queue.append(value)
        print(value, "inserted into queue")

    def dequeue(self):
        if len(self.queue) == 0:
            print("Queue Underflow")
        else:
            print("Deleted element:", self.queue.pop(0))

    def peek(self):
        if len(self.queue) == 0:
            print("Queue is empty")
        else:
            print("Front element:", self.queue[0])

    def display(self):
        if len(self.queue) == 0:
            print("Queue is empty")
        else:
            print("Queue elements:", self.queue)

q = Queue()

while True:
    print("\n--- Queue Menu ---")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        q.enqueue()
    elif choice == 2:
        q.dequeue()
    elif choice == 3:
        q.peek()
    elif choice == 4:
        q.display()
    elif choice == 5:
        print("Exiting...")
        break
    else:
        print("Invalid choice")