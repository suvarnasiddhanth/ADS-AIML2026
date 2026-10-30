class Circular_Queue:
    def __init__(self, capacity):
        
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = -1
        self.rear = -1
        
    def isFull(self):
        return (self.rear + 1) % self.capacity == self.front
    
    def isEmpty(self):
        return self.front == -1
    
    def enqueue(self, element):
        if self.isFull():
            return "Queue is Full."
        
        if self.isEmpty():
            self.front = 0
        self.rear =  (self.rear + 1) % self.capacity
        self.queue[self.rear] = element
        
    def dequeue(self):
        if self.isEmpty():
            "Queue is Empty."
        
        removed_element = self.queue[self.front]
        self.queue[self.front] = None
        
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        
        return removed_element
    
    def first(self):
        if self.isEmpty():
            return "Queue is Empty."
        return self.queue[self.front]
    
    def size(self):
        if self.isEmpty():
            return "Queue is Empty"
        return (self.rear - self.front + self.capacity) % self.capacity + 1
    
    def display(self):
        if self.isEmpty():
            return "Queue is Empty."
        
        result = []
        i = self.front
        while True:
            result.append(self.queue[i])
            if i == self.rear:
                break
            i = (i + 1) % self.capacity
        return result


if __name__ == '__main__':
    
    capacity = int(input("Enter the capacity of the Circular Queue : "))
    myQueue = Circular_Queue(capacity)
    
while True:
    print("Circular Queue Operations : ")
    print("1. Enqueue\n2. Dequeue\n3. First\n4. IsEmpty\n5. Size\n6. Display\n7. Exit ")
    
    try:
        choice = int(input("Enter your choice : "))
    except ValueError:
        print("Invalid Choice\n")
        continue
        
    match choice:
        case 1:
            if myQueue.isFull():
                print("Queue is Full.")
            else:
                element = int(input("Enter an element to insert into Queue : "))
                myQueue.enqueue(element)
        case 2:
            if myQueue.isEmpty():
                    print("Queue is Empty.")
            else:
                print("Deleted element from Queue : ", myQueue.dequeue())
        case 3:
            if len(myQueue.queue) == 0:
                print("Queue is Empty.")
            else:
                print("First element of Queue : ", myQueue.first())
        case 4:
            print("Queue is Empty : ", myQueue.isEmpty())
        case 5:
            print("Size of Queue : ", myQueue.size())
        case 6:
            print("Queue : ", myQueue.queue)
        case 7:
            break
        case _:
            print("Invalid choice.")

print("Program exited Successfully")
            
    


        