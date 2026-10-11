
from collections import deque


class FlexibleQueue:
    def __init__(self):
        self.items = deque()

    def insert_front(self, data):
        self.items.appendleft(data)
        print(f"{data} inserted at the front.")

    def insert_rear(self, data):
        self.items.append(data)
        print(f"{data} inserted at the rear.")

    def delete_front(self):
        if self.is_empty():
            print("Queue is empty!")
            return

        print("Deleted from front:", self.items.popleft())

    def delete_rear(self):
        if self.is_empty():
            print("Queue is empty!")
            return

        print("Deleted from rear:", self.items.pop())

    def display(self):
        if self.is_empty():
            print("Queue is empty!")
            return

        print("Queue (front to rear):", list(self.items))

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        print("Queue size:", len(self.items))


def flexible_queue_menu():
    queue = FlexibleQueue()

    while True:
        print("\n--- FLEXIBLE QUEUE MENU ---")
        print("1. Insert at front")
        print("2. Insert at rear")
        print("3. Delete from front")
        print("4. Delete from rear")
        print("5. Display")
        print("6. Check if empty")
        print("7. Size")
        print("8. Back to main menu")

        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                data = int(input("Enter data: "))
                queue.insert_front(data)

            elif choice == "2":
                data = int(input("Enter data: "))
                queue.insert_rear(data)

            elif choice == "3":
                queue.delete_front()

            elif choice == "4":
                queue.delete_rear()

            elif choice == "5":
                queue.display()

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
