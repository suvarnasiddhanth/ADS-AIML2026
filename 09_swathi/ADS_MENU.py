
from singly_linked_list import singly_linked_list_menu
from doubly_linked_list import doubly_linked_list_menu
from stack import stack_menu
from queue import queue_menu
from flexible_queue import flexible_queue_menu


def main_menu():
    while True:
        print("\n========== ADS LAB MENU ==========")
        print("1. Singly Linked List (SL)")
        print("2. Doubly Linked List (DL)")
        print("3. Stack")
        print("4. Queue")
        print("5. Flexible Queue")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            singly_linked_list_menu()
        elif choice == "2":
            doubly_linked_list_menu()
        elif choice == "3":
            stack_menu()
        elif choice == "4":
            queue_menu()
        elif choice == "5":
            flexible_queue_menu()
        elif choice == "6":
            print("Exiting ADS Lab. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()
