
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def enqueue(self, val):
        node = Node(val)

        if self.rear is None:
            self.front = self.rear = node
        else:
            self.rear.next = node
            self.rear = node

        self.size += 1

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty!")
            return None

        dequeued_node = self.front
        self.front = self.front.next
        self.size -= 1

        if self.front is None:
            self.rear = None

        return dequeued_node.data

    def peek(self):
        if self.isEmpty():
            print("Queue is empty!")
            return None

        return self.front.data

    def isEmpty(self):
        return self.size == 0

    def traverseAndPrint(self):
        if self.isEmpty():
            print("Queue is empty!")
            return

        current = self.front

        while current:
            print(current.data, end=" -> ")
            current = current.next

        print("None")

    def queueSize(self):
        return self.size


# Menu-driven program
myQueue = Queue()

while True:
    print("\n----- QUEUE MENU -----")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display Queue")
    print("5. Check if Queue is Empty")
    print("6. Queue Size")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        val = input("Enter value to insert: ")
        myQueue.enqueue(val)
        print(val, "inserted into the queue.")

    elif choice == '2':
        result = myQueue.dequeue()
        if result is not None:
            print("Dequeued element:", result)

    elif choice == '3':
        result = myQueue.peek()
        if result is not None:
            print("Front element:", result)

    elif choice == '4':
        print("Queue: ", end="")
        myQueue.traverseAndPrint()

    elif choice == '5':
        print("Queue is empty:", myQueue.isEmpty())

    elif choice == '6':
        print("Queue size:", myQueue.queueSize())

    elif choice == '7':
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")
