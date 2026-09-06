class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, element):
        self.queue.append(element)
    def dequeue(self):
        if self.isEmpty():
            return "Queue is Empty."
        return self.queue.pop(0)
    
    def peek(self):
        if self.isEmpty():
            return None
        return self.queue[0]

    def isEmpty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)
    
myQueue = Queue()

m = "1"
while(m == "1"):
    print("1. Enqueue\n2. Dequeue\n3. Peek\n4. IsEmpty\n5. Size\n6. Print Queue")
    choice = int(input("Enter your choice : "))
    
    match choice:
        case 1:
            element = int(input("Enter an element to insert into Queue : "))
            myQueue.enqueue(element)
        case 2:
            if len(myQueue.queue) == 0:
                print("Queue is Empty.")
            else:
                print("Deleted element from Queue : ", myQueue.dequeue())
        case 3:
            if len(myQueue.queue) == 0:
                print("Queue is Empty.")
            else:
                print("Peek element of Queue : ", myQueue.peek())
        case 4:
            print("Queue is Empty : ", myQueue.isEmpty())
        case 5:
            print("Size of Queue : ", myQueue.size())
        case 6:
            print("Queue : ", myQueue.queue)
        case _:
            print("Invalid choice.")
        
    while True:
        m = input("Do you want to continue operation (Yes = 1 / No = 0) : ")
        if m in ("1", "0"):
            break
        else:
            print("Wrong Choice! Please enter only 1 and 0.")
            
print("Program exited Successfully.")