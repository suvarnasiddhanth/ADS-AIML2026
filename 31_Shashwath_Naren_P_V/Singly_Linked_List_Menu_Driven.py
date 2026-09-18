class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __repr__(self):
        return f"Node({self.data})"
    
    
class Singly_Linked_List:
    def __init__(self):
        self.head = None
        
    def insert_at_beginning(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
        
    def insert_at_end(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = newNode
    
    def insert_at_index(self, data, index):
        
        length = 0
        current = self.head
        while current:
            length += 1
            current = current.next
            
        if index < 0 or index > length:
            print("Index out of range")
            return
        
        if index == 0:
            self.insert_at_beginning(data)
            return

        current = self.head
            # Traverse until we reach the node right before our target index
        for _ in range(index - 1):
            if current is None or current.next is None:
                 break
            current = current.next

        if current is None:
            return "Index out of range"

        newNode = Node(data)
        newNode.next = current.next
        current.next = newNode

        
    def delete_from_beginning(self):
        if self.head is None:
            return "The List is empty"
        self.head = self.head.next
    
    def delete_from_end(self):
        if self.head is None:
            return "The List is empty"
        if self.head.next is None:
            self.head = None
            return
        
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None


    def delete_from_index(self, index):
        length = 0
        current = self.head

        while current:
            length += 1
            current = current.next

        if index < 0 or index >= length:
            print("Index out of range")
            return

        if index == 0:
            self.delete_from_beginning
            return

        current = self.head
        for _ in range(index - 1):
            current = current.next

        current.next = current.next.next

        
    def search(self, value):
        current = self.head
        position = 0
        while current:
            if str(current.data) == str(value):
                return f"Value : '{value}' found at the position '{position}'"
            current = current.next
            position += 1
        return f"Value '{value}' not found in the list"
        
    def traverse(self):
        current = self.head
        while current: 
            print(current.data, " <->", end = " ")
            current = current.next   
        print("None")


List = Singly_Linked_List()


while(True):
    
    print("Singly Linked List Operations : ")
    print("\n1. Insert at beginning\n2. Insert at end\n3. Insert at index\n4. Delete from beginning\n5. Delete from end\n6. Delete from index\n7. Search an element\n8. Traverse\n9. Quit")
    
    try:
        choice = int(input("Enter your choice : "))
    except ValueError:
        print("Invalid Choice\n")
        continue          
   
    
    match choice:
      
        case 1 : 
            element = input("Enter an element to insert at the beginning of the Linked List : ")
            List.insert_at_beginning(element)
        case 2:
            element = input("Enter an element to insert at the end of the Linked List : ")
            List.insert_at_end(element)
        case 3:
                element = input("Enter an element to insert at the index position of the Linked List : ")
                
                try:
                    index   = int(input("Enter the index position :  "))
                except ValueError:
                    print("Invalid index position. Returning to Menu.\n")
                    continue
                List.insert_at_index(element, index)
        case 4 : 
                List.delete_from_beginning()
        case 5 : 
                List.delete_from_end()
        case 6 :
                try:
                    index   = int(input("Enter the index position :  "))
                except ValueError:
                    print("Invalid index position. Returning to Menu.\n")
                    continue
                List.insert_at_index(element, index)
        case 7 : 
                element = input("Enter an element to search in the Linked List : ")   
                print(List.search(element))
        case 8:
            List.traverse() 
        case 9 : exit()
        case _ : 
            print("Invalid Choice")
            
print("Program exited Successfully.")
