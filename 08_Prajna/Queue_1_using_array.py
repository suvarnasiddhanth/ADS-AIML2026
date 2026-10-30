class Queue:
    def __init__(self, capacity):
        self.capacity = capacity  # Maximum queue size
        self.queue = []           # Array to store elements

    # 1. Enqueue: Insert an element at the rear
    def enqueue(self, data):
        if self.isFull():
            print("Queue Overflow")
        else:
            self.queue.append(data)   # Add element at the end
            print("Inserted:", data)

    # 2. Dequeue: Remove an element from the front
    def dequeue(self):
        if self.isEmpty():
            print("Queue Underflow")
        else:
            data = self.queue.pop(0)  # Remove first element
            print("Removed:", data)

    def peek(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            print("Front element:", self.queue[0])

    def display(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            print("Queue (front to rear):", self.queue)

    def size(self):
        return len(self.queue)

    def search(self, data):
        for i in range(len(self.queue)):
            if self.queue[i] == data:
                print("Element found at index:", i)
                return
        print("Element not found")

    def isEmpty(self):
        return len(self.queue) == 0

    def isFull(self):
        return len(self.queue) == self.capacity

def queue_array_menu():
    capacity = int(input("Enter queue capacity: "))
    q = Queue(capacity)

    while True:
        print("\n--- QUEUE USING ARRAY ---")
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
            data = int(input("Enter value: "))
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
            data = int(input("Enter value to search: "))
            q.search(data)

        elif choice == "7":
            print("Queue is empty:", q.isEmpty())

        elif choice == "8":
            print("Queue is full:", q.isFull())

        elif choice == "9":
            print("Exiting program")
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    queue_array_menu()