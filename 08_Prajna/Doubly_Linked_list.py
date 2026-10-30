class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

head = None

def insertFront(data):
    global head
    newNode = Node(data)
    if head is None:
        head = newNode
    else:
        newNode.next = head
        head.prev = newNode
        head = newNode

def insertEnd(data):
    global head
    newNode = Node(data)

    if head is None:
        head = newNode
        return
    
    curr = head

    while curr.next is not None:
        curr = curr.next
        
    curr.next = newNode
    newNode.prev = curr

def insertPosition(data, position):
    global head
    if position < 0:
        print("Invalid position!")
        return
    if position == 0:
        insertFront(data)
        return
    curr = head
    index = 0

    while curr is not None and index < position - 1:
        curr = curr.next
        index += 1

    if curr is None:
        print("Invalid position!")
        return
    
    newNode = Node(data)
    newNode.next = curr.next
    newNode.prev = curr

    if curr.next is not None:
        curr.next.prev = newNode

    curr.next = newNode

def deleteFront():
    global head

    if head is None:
        print("List is empty")
        return

    head = head.next

    # The new first node has no previous node
    if head is not None:
        head.prev = None

def deleteEnd():
    global head

    if head is None:
        print("List is empty")
        return

    # Only one node exists
    if head.next is None:
        head = None
        return

    curr = head

    # Reach the last node
    while curr.next is not None:
        curr = curr.next

    # Remove the last node
    curr.prev.next = None

def deletePosition(position):
    global head

    if position < 0:
        print("Invalid position!")
        return

    # Delete at front
    if position == 0:
        deleteFront()
        return

    curr = head
    index = 0

    # Reach the node to be deleted
    while curr is not None and index < position:
        curr = curr.next
        index += 1

    if curr is None:
        print("Invalid position!")
        return

    # Connect the previous node to the next node
    curr.prev.next = curr.next

    # Update the next node's previous pointer
    if curr.next is not None:
        curr.next.prev = curr.prev

def search(data):
    curr = head
    position = 0

    while curr is not None:
        if curr.data == data:
            print("Element found at position", position)
            return

        curr = curr.next
        position += 1

    print("Element not found")

def countNodes():
    curr = head
    count = 0

    while curr is not None:
        count += 1
        curr = curr.next

    print("Total number of nodes:", count)

# 10. DISPLAY FORWARD
def display():
    curr = head

    if curr is None:
        print("List is empty")
        return

    while curr is not None:
        print(curr.data, end=" <-> ")
        curr = curr.next

    print("None")

# 11. DISPLAY BACKWARD
def displayBackward():
    curr = head

    if curr is None:
        print("List is empty")
        return

    # Reach the last node
    while curr.next is not None:
        curr = curr.next

    # Traverse backward using prev
    while curr is not None:
        print(curr.data, end=" <-> ")
        curr = curr.prev

    print("None")

def reverseList():
    global head

    curr = head
    newHead = None

    while curr is not None:
        # Swap the next and previous pointers
        curr.prev, curr.next = curr.next, curr.prev

        # Save the current node as the new head candidate
        newHead = curr

        # After swapping, curr.prev points to the old next node
        curr = curr.prev

    head = newHead
    print("Linked list reversed successfully!")

def doubly_linked_list_menu():
    while True:
        print("\n===== DOUBLY LINKED LIST =====")
        print("1. Insert at the front")
        print("2. Insert at the end")
        print("3. Insert at a specific position")
        print("4. Delete at the front")
        print("5. Delete at the end")
        print("6. Delete at a specific position")
        print("7. Search for a value")
        print("8. Count nodes")
        print("9. Display forward")
        print("10. Display backward")
        print("11. Reverse the list")
        print("12. Exit")
        
        choice = int(input("Enter the choice: "))
        
        if choice == 1:
            data = int(input("Enter value: "))
            insertFront(data)
        
        elif choice == 2:
            data = int(input("Enter value: "))
            insertEnd(data)
        
        elif choice == 3:
            data = int(input("Enter value: "))
            position = int(input("Enter position (starting from 0): "))
            insertPosition(data, position)
        
        elif choice == 4:
            deleteFront()
        
        elif choice == 5:
            deleteEnd()
        
        elif choice == 6:
            position = int(input("Enter position to delete: "))
            deletePosition(position)
        
        elif choice == 7:
            data = int(input("Enter value to search: "))
            search(data)
        
        elif choice == 8:
            countNodes()
        
        elif choice == 9:
            display()
    
        elif choice == 10:
            displayBackward()
        
        elif choice == 11:
            reverseList()
            display()
        
        elif choice == 12:
            print("Program terminated.")
            break
        
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    doubly_linked_list_menu()