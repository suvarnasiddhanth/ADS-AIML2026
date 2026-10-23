from SinglyLL import SinglyLinkedList
from DoublyLL import DoublyLinkedList
from Astack import Stack
from AQueue import Queue


def singly_menu():
    sll = SinglyLinkedList()

    while True:
        print("\n--- SINGLY LINKED LIST ---")
        print("1. Insert")
        print("2. Delete")
        print("3. Display")
        print("4. Back to Main Menu")

        ch = input("Enter choice: ")

        if ch == '1':
            data = int(input("Enter value: "))
            sll.insert(data)
        elif ch == '2':
            data = int(input("Enter value to delete: "))
            sll.delete(data)
        elif ch == '3':
            sll.display()
        elif ch == '4':
            break
        else:
            print("Invalid choice.")


def doubly_menu():
    dll = DoublyLinkedList()

    while True:
        print("\n--- DOUBLY LINKED LIST ---")
        print("1. Insert")
        print("2. Delete")
        print("3. Display Forward")
        print("4. Display Reverse")
        print("5. Back to Main Menu")

        ch = input("Enter choice: ")

        if ch == '1':
            data = int(input("Enter value: "))
            dll.insert(data)
        elif ch == '2':
            data = int(input("Enter value to delete: "))
            dll.delete(data)
        elif ch == '3':
            dll.display()
        elif ch == '4':
            dll.display_reverse()
        elif ch == '5':
            break
        else:
            print("Invalid choice.")


def stack_menu():
    st = Stack()

    while True:
        print("\n--- STACK ---")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Display")
        print("5. Back to Main Menu")

        ch = input("Enter choice: ")

        if ch == '1':
            data = int(input("Enter value: "))
            st.push(data)
        elif ch == '2':
            st.pop()
        elif ch == '3':
            st.peek()
        elif ch == '4':
            st.display()
        elif ch == '5':
            break
        else:
            print("Invalid choice.")


def queue_menu():
    q = Queue()

    while True:
        print("\n--- QUEUE ---")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Front")
        print("4. Display")
        print("5. Back to Main Menu")

        ch = input("Enter choice: ")

        if ch == '1':
            data = int(input("Enter value: "))
            q.enqueue(data)
        elif ch == '2':
            q.dequeue()
        elif ch == '3':
            q.front()
        elif ch == '4':
            q.display()
        elif ch == '5':
            break
        else:
            print("Invalid choice.")


def main():
    while True:
        print("\n====== DATA STRUCTURES MENU ======")
        print("1. Singly Linked List")
        print("2. Doubly Linked List")
        print("3. Stack")
        print("4. Queue")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            singly_menu()
        elif choice == '2':
            doubly_menu()
        elif choice == '3':
            stack_menu()
        elif choice == '4':
            queue_menu()
        elif choice == '5':
            print("Program terminated.")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
