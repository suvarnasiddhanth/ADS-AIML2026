"""
Queue using a Singly Linked List (FIFO = First In, First Out)

(The file is called queue_ll.py, not queue.py, because Python already has a
built-in module named "queue" and a file with the same name would hide it.)

Run on its own:     python queue_ll.py
Or from main menu:  python main.py
"""


class Node:
    def __init__(self, data):
        self.data = data    # value stored
        self.next = None    # link to the next node


class Queue:
    def __init__(self):
        self.head = None    # FRONT: items leave from here
        self.tail = None    # REAR: items join here
        self.size = 0

    def is_empty(self):                 # O(1)
        return self.head is None

    def enqueue(self, data):            # O(1)
        new_node = Node(data)
        if not self.tail:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def dequeue(self):                  # O(1)
        if not self.head:
            return None
        value = self.head.data
        self.head = self.head.next
        if not self.head:
            self.tail = None
        self.size -= 1
        return value

    def peek(self):                     # O(1)
        return self.head.data if self.head else None

    def display(self):                  # O(n)
        if self.is_empty():
            print("Queue is empty.")
            return
        current = self.head
        print("FRONT ->", end=" ")
        while current:
            print(current.data, end=" ")
            current = current.next
        print("<- REAR")


# ---------------------------------------------------------------------
# Menu
# ---------------------------------------------------------------------
def read_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a whole number.")


my_queue = Queue()      # created once, so the data stays when you go back to the main menu


def menu():
    while True:
        print("\n------ QUEUE (Linked List) ------")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek (front element)")
        print("4. Display")
        print("5. Size")
        print("6. Is empty?")
        print("0. Back")
        choice = read_int("Enter choice: ")

        if choice == 1:
            value = read_int("Enter value to enqueue: ")
            my_queue.enqueue(value)
            print(value, "enqueued.")
        elif choice == 2:
            if my_queue.is_empty():
                print("Queue underflow! The queue is empty.")
            else:
                print("Dequeued:", my_queue.dequeue())
        elif choice == 3:
            if my_queue.is_empty():
                print("Queue is empty.")
            else:
                print("Front element:", my_queue.peek())
        elif choice == 4:
            my_queue.display()
        elif choice == 5:
            print("Size:", my_queue.size)
        elif choice == 6:
            if my_queue.is_empty():
                print("Yes, the queue is empty.")
            else:
                print("No, the queue is not empty.")
        elif choice == 0:
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    menu()
