
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, data):
        self.items.append(data)
        print(f"{data} inserted into the queue.")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty! Cannot dequeue.")
            return

        print("Deleted element:", self.items.pop(0))

    def front(self):
        if self.is_empty():
            print("Queue is empty!")
            return

        print("Front element:", self.items[0])

    def rear(self):
        if self.is_empty():
            print("Queue is empty!")
            return

        print("Rear element:", self.items[-1])

    def display(self):
        if self.is_empty():
            print("Queue is empty!")
            return

        print("Queue (front to rear):", self.items)

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        print("Queue size:", len(self.items))


def queue_menu():
    queue = Queue()

    while True:
        print("\n--- QUEUE MENU ---")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Display")
        print("4. View front")
        print("5. View rear")
        print("6. Check if empty")
        print("7. Size")
        print("8. Back to main menu")

        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                data = int(input("Enter data: "))
                queue.enqueue(data)

            elif choice == "2":
                queue.dequeue()

            elif choice == "3":
                queue.display()

            elif choice == "4":
                queue.front()

            elif choice == "5":
                queue.rear()

            elif choice == "6":
                print(
                    "Queue is empty."
                    if queue.is_empty()
                    else "Queue is not empty."
                )

            elif choice == "7":
                queue.size()

            elif choice == "8":
                break

            else:
                print("Invalid choice!")

        except ValueError:
            print("Please enter a valid integer.")
