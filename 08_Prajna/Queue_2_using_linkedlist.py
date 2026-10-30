class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Create the Queue
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.count = 0

    # ENQUEUE: Insert at rear
    def enqueue(self, data):
        new_node = Node(data)

        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

        self.count += 1
        print("Inserted:", data)

    # DEQUEUE: Remove from front
    def dequeue(self):
        if self.isEmpty():
            print("Queue Underflow")
        else:
            print("Removed:", self.front.data)
            self.front = self.front.next
            self.count -= 1

            # If queue becomes empty, reset rear
            if self.front is None:
                self.rear = None

    # PEEK: Display front element
    def first(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            print("Front element:", self.front.data)

    # DISPLAY: Show all elements
    def display(self):
        if self.isEmpty():
            print("Queue is empty")
            return

        current = self.front
        print("Queue (front to rear):", end=" ")

        while current:
            print(current.data, end=" -> ")
            current = current.next

        print("None")

    # SIZE: Count elements
    def size(self):
        return self.count

    # SEARCH: Find an element
    def search(self, data):
        current = self.front
        index = 0

        while current:
            if current.data == data:
                print("Element found at index:", index)
                return

            current = current.next
            index += 1

        print("Element not found")

    # Check if queue is empty
    def isEmpty(self):
        return self.front is None

def queue_linked_list_menu():
    # Create a queue
    q = Queue()

    while True:
        print("\n--- QUEUE USING LINKED LIST ---")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. First")
        print("4. Display")
        print("5. Size")
        print("6. Search")
        print("7. isEmpty")
        print("8. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            data = input("Enter element: ")
            q.enqueue(data)

        elif choice == "2":
            q.dequeue()

        elif choice == "3":
            q.first()

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
            print("Exiting program")
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    queue_linked_list_menu()