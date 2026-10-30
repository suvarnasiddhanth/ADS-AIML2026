from LinkedList import LinkedListMenu
from QueueUsingLinkedList import QueueMenu
from StackUsingLinkedList import StackMenu

def main():

    while True:

        print("\n===== DATA STRUCTURE MENU =====")
        print("1. Linked List")
        print("2. Stack")
        print("3. Queue")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            LinkedListMenu()

        elif choice == 2:
            StackMenu()

        elif choice == 3:
            QueueMenu()

        elif choice == 4:
            print("Program terminated")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()