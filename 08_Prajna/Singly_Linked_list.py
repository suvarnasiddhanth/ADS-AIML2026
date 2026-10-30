class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = None

# 2. INSERT AT THE BEGINNING
def insertFront(data):
    global head

    newNode = Node(data)
    newNode.next = head
    head = newNode

# 3. INSERT AT THE END
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

# 4. INSERT AT A SPECIFIC POSITION (0-BASED)
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

    # Reach the node before the required position
    while curr is not None and index < position - 1:
        curr = curr.next
        index += 1

    if curr is None:
        print("Invalid position!")
        return

    newNode = Node(data)
    newNode.next = curr.next
    curr.next = newNode

# 5. DELETE FROM THE BEGINNING
def deleteFront():
    global head

    if head is None:
        print("List is empty")
        return
    head = head.next

# 6. DELETE FROM THE END
def deleteEnd():
    global head

    if head is None:
        print("List is empty")
        return
    if head.next is None:
        head = None
        return

    curr = head

    while curr.next.next is not None:
        curr = curr.next

    curr.next = None

# 7. DELETE AT A SPECIFIC POSITION (0-BASED)
def deletePosition(position):
    global head

    if position < 0:
        print("Invalid position!")
        return

    # Delete the first node
    if position == 0:
        deleteFront()
        return

    curr = head
    index = 0

    # Reach the node before the target
    while curr is not None and index < position - 1:
        curr = curr.next
        index += 1

    # Target position does not exist
    if curr is None or curr.next is None:
        print("Invalid position!")
        return

    # Skip the node to be deleted
    curr.next = curr.next.next

# 8. SEARCH FOR A VALUE
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

# 9. COUNT THE NUMBER OF NODES
def countNodes():
    curr = head
    count = 0

    while curr is not None:
        count += 1
        curr = curr.next

    print("Total number of nodes:", count)

# 10. DISPLAY THE LINKED LIST
def display():
    curr = head

    if curr is None:
        print("List is empty")
        return

    while curr is not None:
        print(curr.data, end=" -> ")
        curr = curr.next

    print("None")


# 11. REVERSE THE LINKED LIST
def reverseList():
    global head

    prev = None
    curr = head

    while curr is not None:
        nextNode = curr.next  # Save the next node
        curr.next = prev      # Reverse the link
        prev = curr           # Move prev forward
        curr = nextNode       # Move curr forward

    head = prev               # Update the head
    print("Linked list reversed successfully!")

def singly_linked_list_menu():
    while True:
        print("\n===== SINGLY LINKED LIST =====")
        print("1. Insert at the beginning")
        print("2. Insert at the end")
        print("3. Insert at a specific position")
        print("4. Delete from the beginning")
        print("5. Delete from the end")
        print("6. Delete at a specific position")
        print("7. Search for a value")
        print("8. Count nodes")
        print("9. Display")
        print("10. Reverse the linked list")
        print("11. Exit")
    
        choice = int(input("Enter choice: "))
        
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
            position = int(input("Enter position to delete (starting from 0): "))
            deletePosition(position)
    
        elif choice == 7:
            data = int(input("Enter value to search: "))
            search(data)
        
        elif choice == 8:
            countNodes()
        
        elif choice == 9:
            display()
        
        elif choice == 10:
            reverseList()
            display()
        
        elif choice == 11:
            print("Program terminated.")
            break
        
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    singly_linked_list_menu()