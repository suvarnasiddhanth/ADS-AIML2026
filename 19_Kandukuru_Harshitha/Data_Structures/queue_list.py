class Queue_list:
    def __init__(self):
        self.queue = []
    def enqueue(self,item):
        self.queue.append(item)
        print("Enqueued element:", item)
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty, nothing to dequeue()")
        else:
            a = self.queue.pop(0)
            print("Dequeued element:", a)
    def is_empty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False
    def display(self):
        print("Queue elements:", self.queue)
    def front_display(self):
        if self.is_empty():
            print("Queue is empty, no front element")
        else:
            print("Front element:", self.queue[0])
    def rear_display(self):
        if self.is_empty():
            print("Queue is empty, no rear element")
        else:
            print("Rear element:", self.queue[-1])
    def size(self):
        print("Size of the queue:", len(self.queue))

def main():
    queue = Queue_list()
    while True:
        print("\nQueue Operations Menu:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Display")
        print("4. Front Display")
        print("5. Rear Display")
        print("6. Size")
        print("7. Exit")
        choice = int(input("Enter your choice (1-7): "))
        if choice == 1:
            item = int(input("Enter the element to enqueue: "))
            queue.enqueue(item)
        elif choice == 2:
            queue.dequeue()
        elif choice == 3:
            queue.display()
        elif choice == 4:
            queue.front_display()
        elif choice == 5:
            queue.rear_display()
        elif choice == 6:
            queue.size()
        elif choice == 7:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()