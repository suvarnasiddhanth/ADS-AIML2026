class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue.pop(0)

    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def display(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print(self.queue)



def main():
    q = Queue()

    while True:
        print("\n----- QUEUE MENU -----")
        print("1. Enqueue (add item)")
        print("2. Dequeue (remove item)")
        print("3. Peek (view front item)")
        print("4. Display queue")
        print("5. Check if empty")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            item = input("Enter item to enqueue: ")
            q.enqueue(item)
            print("{item} added to the queue.")

        elif choice == "2":
            result = q.dequeue()
            print("Dequeued: {result}")

        elif choice == "3":
            result = q.peek()
            print("Front item: {result}")

        elif choice == "4":
            print("Current queue:")
            q.display()

        elif choice == "5":
            print("Queue is empty." if q.is_empty() else "Queue is not empty.")

        elif choice == "6":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice! Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()