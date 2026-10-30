class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = -1
        self.rear = -1
        self.count = 0

    # ENQUEUE: Insert an element
    def enqueue(self, data):
        if self.isFull():
            print("Queue Overflow")
            return

        if self.isEmpty():
            self.front = 0

        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = data
        self.count += 1
        print("Inserted:", data)

    # DEQUEUE: Remove the front element
    def dequeue(self):
        if self.isEmpty():
            print("Queue Underflow")
            return

        print("Removed:", self.queue[self.front])
        self.queue[self.front] = None
        self.count -= 1

        if self.count == 0:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity

    # PEEK: Display the front element
    def peek(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            print("Front element:", self.queue[self.front])

    # DISPLAY: Show elements from front to rear
    def display(self):
        if self.isEmpty():
            print("Queue is empty")
            return

        print("Queue (front to rear):", end=" ")

        for i in range(self.count):
            index = (self.front + i) % self.capacity
            print(self.queue[index], end=" ")

        print()

    # SIZE: Return number of elements
    def size(self):
        return self.count

    # SEARCH: Find an element
    def search(self, data):
        for i in range(self.count):
            index = (self.front + i) % self.capacity

            if self.queue[index] == data:
                print("Element found at index:", index)
                return

        print("Element not found")

    # Check if queue is empty
    def isEmpty(self):
        return self.count == 0

    # Check if queue is full
    def isFull(self):
        return self.count == self.capacity

def queue_circular_menu():
    # Create a circular queue
    capacity = int(input("Enter queue capacity: "))
    q = CircularQueue(capacity)
    # Main menu
    while True:
        print("\n--- CIRCULAR QUEUE ---")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek")
        print("4. Display")
        print("5. Size")
        print("6. Search")
        print("7. isEmpty")
        print("8. isFull")
        print("9. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            data = input("Enter element: ")
            q.enqueue(data)

        elif choice == "2":
            q.dequeue()

        elif choice == "3":
            q.peek()

        elif choice == "4":
            q.display()

        elif choice == "5":
            print("Queue size:", q.size())

        elif choice == "6":
            data = input("Enter element to search: ")
            q.search(data)

        elif choice == "7":
            print("Is empty:", q.isEmpty())

        elif choice == "8":
            print("Is full:", q.isFull())

        elif choice == "9":
            print("Exiting program")
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    queue_circular_menu()