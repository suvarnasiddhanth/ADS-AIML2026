class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __repr__(self):
        return f"Node({self.data})"
    
class Linked_List:
    def __init__(self):
        self.head = None
    
    def insert_at_end(self, data):
        
        newNode = Node(data)
        
        if self.head is None:
            self.head = newNode
            return

        last = self.head
        while last.next:
            last = last.next
        last.next = newNode
    
    def split(self):
        if self.head is None:
            return None
        if self.head.next is None:
            second_queue = None
        else:
            slow = self.head
            fast = self.head
        
            while fast.next and fast.next.next:
                fast = fast.next.next
                slow = slow.next
            
            second_queue = slow.next
            slow.next = None

        print("Food Truck 1 : ", end = "")
        current = self.head
        while current:
            print(current.data, end = " -> " if current.next else "")
            current = current.next
        print()
            
        print("Food Truck 2 : ", end ="")
        current = second_queue
        while current:
            print(current.data, end = " -> " if current.next else "")
            current = current.next
        print()

    def traverse(self):
        current = self.head
        print("Food Truck 1 : ", end = "")
        while current:
            print(current.data, "<->", end = " ")
            current = current.next
        print(": Food Truck 2")
        
        
if __name__ == "__main__":
    
    linked_list = Linked_List()

n = int(input("Enter total number of people : "))
while True:
    if n > 0:
        break
    else:
        print("Please enter a number greater than 0")
    
for i in range(1, n+1):
    linked_list.insert_at_end(i)

print("\nBefore Split :")
linked_list.traverse()

print("\nAfter Split :")
linked_list.split()
    
    
        