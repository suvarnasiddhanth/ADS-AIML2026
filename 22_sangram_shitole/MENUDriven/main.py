
# ==========================================
# MENU DRIVEN DATA STRUCTURE PROGRAM
# ==========================================

from Stack import Stack
from Circular import CircularLinkedList
from queue import Queue
from LinkedList import LinkedList
from DoublyLinkedList import DoublyLinkedList


# ==========================================
# MENU FUNCTIONS
# ==========================================

    
def main_menu():
    print("\n")
    print("========================================")
    print("       DATA STRUCTURE MENU")
    print("========================================")
    print("1. Stack")
    print("2. Queue")
    print("3. Singly Linked List")
    print("4. Doubly Linked List")
    print("5. Circular Linked List")
    print("6. Exit")
    print("========================================")


def stack_menu():
    print("\n")
    print("========================================")
    print("              STACK")
    print("========================================")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Size")
    print("5. Is Empty")
    print("6. Display")
    print("7. Back to Main Menu")
    print("========================================")


def queue_menu():
    print("\n")
    print("========================================")
    print("              QUEUE")
    print("========================================")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Rear")
    print("5. Size")
    print("6. Is Empty")
    print("7. Display")
    print("8. Back to Main Menu")
    print("========================================")


def linked_list_menu():
    print("\n")
    print("========================================")
    print("          SINGLY LINKED LIST")
    print("========================================")
    print("1. Insert at Beginning")
    print("2. Insert at End")
    print("3. Insert at Position")
    print("4. Delete at Beginning")
    print("5. Delete at End")
    print("6. Delete at Position")
    print("7. Search")
    print("8. Size")
    print("9. Is Empty")
    print("10. Display")
    print("11. Back to Main Menu")
    print("========================================")


def doubly_linked_list_menu():
    print("\n")
    print("========================================")
    print("          DOUBLY LINKED LIST")
    print("========================================")
    print("1. Insert at Beginning")
    print("2. Insert at End")
    print("3. Insert at Position")
    print("4. Delete at Beginning")
    print("5. Delete at End")
    print("6. Delete at Position")
    print("7. Search")
    print("8. Size")
    print("9. Is Empty")
    print("10. Display Forward")
    print("11. Display Backward")
    print("12. Back to Main Menu")
    print("========================================")

def circular_linked_list_menu():
    print("\n")
    print("========================================")
    print("        CIRCULAR LINKED LIST")
    print("========================================")
    print("1. Insert at Beginning")
    print("2. Insert at End")
    print("3. Insert at Position")
    print("4. Delete at Beginning")
    print("5. Delete at End")
    print("6. Delete at Position")
    print("7. Search")
    print("8. Size")
    print("9. Is Empty")
    print("10. Display")
    print("11. Back to Main Menu")
    print("========================================")

# ==========================================
# CREATE DATA STRUCTURE OBJECTS
# ==========================================

stack = Stack()
queue = Queue()
linked_list = LinkedList()
doubly_linked_list = DoublyLinkedList()
circular_linked_list = CircularLinkedList()


# ==========================================
# MAIN PROGRAM
# ==========================================

while True:

    main_menu()

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number.")
        continue


    # ======================================
    # STACK
    # ======================================

    if choice == 1:

        while True:

            stack_menu()

            try:
                operation = int(input("Enter your choice: "))
            except ValueError:
                print("Please enter a valid number.")
                continue


            if operation == 1:
                data = input("Enter element to push: ")
                stack.push(data)
                print("Element pushed successfully.")


            elif operation == 2:
                data = stack.pop()

                if data is not None:
                    print("Popped element:", data)


            elif operation == 3:
                data = stack.peek()

                if data is not None:
                    print("Top element:", data)


            elif operation == 4:
                print("Stack size:", stack.size())


            elif operation == 5:
                if stack.is_empty():
                    print("Stack is empty.")
                else:
                    print("Stack is not empty.")


            elif operation == 6:
                stack.display()


            elif operation == 7:
                break


            else:
                print("Invalid choice.")


    # ======================================
    # QUEUE
    # ======================================

    elif choice == 2:

        while True:

            queue_menu()

            try:
                operation = int(input("Enter your choice: "))
            except ValueError:
                print("Please enter a valid number.")
                continue


            if operation == 1:
                data = input("Enter element to enqueue: ")
                queue.enqueue(data)
                print("Element enqueued successfully.")


            elif operation == 2:
                data = queue.dequeue()

                if data is not None:
                    print("Dequeued element:", data)


            elif operation == 3:
                data = queue.peek()

                if data is not None:
                    print("Front element:", data)


            elif operation == 4:
                data = queue.rear_element()

                if data is not None:
                    print("Rear element:", data)


            elif operation == 5:
                print("Queue size:", queue.size())


            elif operation == 6:
                if queue.is_empty():
                    print("Queue is empty.")
                else:
                    print("Queue is not empty.")


            elif operation == 7:
                queue.display()


            elif operation == 8:
                break


            else:
                print("Invalid choice.")


    # ======================================
    # SINGLY LINKED LIST
    # ======================================

    elif choice == 3:

        while True:

            linked_list_menu()

            try:
                operation = int(input("Enter your choice: "))
            except ValueError:
                print("Please enter a valid number.")
                continue


            if operation == 1:
                data = input("Enter element: ")
                linked_list.insert_at_beginning(data)
                print("Element inserted successfully.")


            elif operation == 2:
                data = input("Enter element: ")
                linked_list.insert_at_end(data)
                print("Element inserted successfully.")


            elif operation == 3:
                data = input("Enter element: ")

                try:
                    position = int(input("Enter position: "))
                    linked_list.insert_at_position(data, position)
                except ValueError:
                    print("Please enter a valid position.")


            elif operation == 4:
                data = linked_list.delete_at_beginning()

                if data is not None:
                    print("Deleted element:", data)


            elif operation == 5:
                data = linked_list.delete_at_end()

                if data is not None:
                    print("Deleted element:", data)


            elif operation == 6:
                try:
                    position = int(input("Enter position: "))
                    data = linked_list.delete_at_position(position)

                    if data is not None:
                        print("Deleted element:", data)

                except ValueError:
                    print("Please enter a valid position.")


            elif operation == 7:
                data = input("Enter element to search: ")

                position = linked_list.search(data)

                if position == -1:
                    print("Element not found.")
                else:
                    print("Element found at position:", position)


            elif operation == 8:
                print("Linked List size:", linked_list.size())


            elif operation == 9:
                if linked_list.is_empty():
                    print("Linked List is empty.")
                else:
                    print("Linked List is not empty.")


            elif operation == 10:
                linked_list.display()


            elif operation == 11:
                break


            else:
                print("Invalid choice.")


    # ======================================
    # DOUBLY LINKED LIST
    # ======================================

    elif choice == 4:

        while True:

            doubly_linked_list_menu()

            try:
                operation = int(input("Enter your choice: "))
            except ValueError:
                print("Please enter a valid number.")
                continue


            if operation == 1:
                data = input("Enter element: ")
                doubly_linked_list.insert_at_beginning(data)
                print("Element inserted successfully.")


            elif operation == 2:
                data = input("Enter element: ")
                doubly_linked_list.insert_at_end(data)
                print("Element inserted successfully.")


            elif operation == 3:
                data = input("Enter element: ")

                try:
                    position = int(input("Enter position: "))
                    doubly_linked_list.insert_at_position(data, position)
                except ValueError:
                    print("Please enter a valid position.")


            elif operation == 4:
                data = doubly_linked_list.delete_at_beginning()

                if data is not None:
                    print("Deleted element:", data)


            elif operation == 5:
                data = doubly_linked_list.delete_at_end()

                if data is not None:
                    print("Deleted element:", data)


            elif operation == 6:
                try:
                    position = int(input("Enter position: "))
                    data = doubly_linked_list.delete_at_position(position)

                    if data is not None:
                        print("Deleted element:", data)

                except ValueError:
                    print("Please enter a valid position.")


            elif operation == 7:
                data = input("Enter element to search: ")

                position = doubly_linked_list.search(data)

                if position == -1:
                    print("Element not found.")
                else:
                    print("Element found at position:", position)


            elif operation == 8:
                print("Doubly Linked List size:",
                      doubly_linked_list.size())


            elif operation == 9:
                if doubly_linked_list.is_empty():
                    print("Doubly Linked List is empty.")
                else:
                    print("Doubly Linked List is not empty.")


            elif operation == 10:
                doubly_linked_list.display_forward()


            elif operation == 11:
                doubly_linked_list.display_backward()


            elif operation == 12:
                break


            else:
                print("Invalid choice.")
    
    elif choice == 5:

     while True:

        circular_linked_list_menu()

        try:
            operation = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if operation == 1:
            data = input("Enter element: ")
            circular_linked_list.insert_at_beginning(data)
            print("Element inserted successfully.")

        elif operation == 2:
            data = input("Enter element: ")
            circular_linked_list.insert_at_end(data)
            print("Element inserted successfully.")

        elif operation == 3:
            data = input("Enter element: ")

            try:
                position = int(input("Enter position: "))
                circular_linked_list.insert_at_position(data, position)
            except ValueError:
                print("Please enter a valid position.")

        elif operation == 4:
            data = circular_linked_list.delete_at_beginning()

            if data is not None:
                print("Deleted element:", data)

        elif operation == 5:
            data = circular_linked_list.delete_at_end()

            if data is not None:
                print("Deleted element:", data)

        elif operation == 6:
            try:
                position = int(input("Enter position: "))
                data = circular_linked_list.delete_at_position(position)

                if data is not None:
                    print("Deleted element:", data)

            except ValueError:
                print("Please enter a valid position.")

        elif operation == 7:
            data = input("Enter element to search: ")

            position = circular_linked_list.search(data)

            if position == -1:
                print("Element not found.")
            else:
                print("Element found at position:", position)

        elif operation == 8:
            print(
                "Circular Linked List size:",
                circular_linked_list.size()
            )

        elif operation == 9:
            if circular_linked_list.is_empty():
                print("Circular Linked List is empty.")
            else:
                print("Circular Linked List is not empty.")

        elif operation == 10:
            circular_linked_list.display()

        elif operation == 11:
            break

        else:
            print("Invalid choice.")


    # ======================================
    # EXIT
    # ======================================

    elif choice == 6:

        print("\nThank you for using the program!")
        print("Exiting...")
        break


    else:
        print("Invalid choice. Please select a number from 1 to 5.")
