class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    def is_empty(self):
        return self.front == -1

    def enqueue(self, data):
        if self.is_full():
            print("Overflow: Queue is full!")
            return

        if self.is_empty():
            self.front = 0

        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = data
        print("Inserted:", data)

    def dequeue(self):
        if self.is_empty():
            print("Underflow: Queue is empty!")
            return None

        deleted = self.queue[self.front]
        self.queue[self.front] = None

        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

        return deleted

    def peek(self):
        if self.is_empty():
            print("Queue is empty!")
            return None

        return self.queue[self.front]

    def get_size(self):
        if self.is_empty():
            return 0

        return (self.rear - self.front + self.size) % self.size + 1

    def display(self):
        if self.is_empty():
            print("Queue is empty!")
            return

        print("Queue elements:", end=" ")

        if self.rear >= self.front:
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
        else:
            for i in range(self.front, self.size):
                print(self.queue[i], end=" ")

            for i in range(0, self.rear + 1):
                print(self.queue[i], end=" ")

        print()

capacity = int(input("Enter the size of the queue: "))
q = Queue(capacity)

m = "1"

while m == "1":
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Is Empty")
    print("5. Size")
    print("6. Print Queue")

    try:
        choice = int(input("Enter your choice: "))

        match choice:
            case 1:
                element = int(input("Enter an element to insert: "))
                q.enqueue(element)

            case 2:
                deleted = q.dequeue()
                if deleted is not None:
                    print("Deleted element:", deleted)

            case 3:
                element = q.peek()
                if element is not None:
                    print("Front element:", element)

            case 4:
                print("Queue is empty:", q.is_empty())

            case 5:
                print("Number of elements:", q.get_size())

            case 6:
                q.display()

            case _:
                print("Invalid choice!")

    except ValueError:
        print("Please enter a valid integer.")

    while True:
        m = input("\nContinue? (1 = Yes / 0 = No): ")

        if m in ("1", "0"):
            break

        print("Wrong choice! Enter only 1 or 0.")

