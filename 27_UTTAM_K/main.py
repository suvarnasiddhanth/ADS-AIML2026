"""
Data Structures and Sorting - Main Menu

Keep all 12 files in the SAME folder, then run:
    python main.py

Each data structure and each sort lives in its own file and has its own menu.
Your data is kept while the program runs, so you can go back to the main
menu and return to an option without losing what you entered.
"""

import stack
import queue_ll
import linked_list
import doubly_linked_list
import tree
import bst
import bubble_sort
import insertion_sort
import merge_sort
import quick_sort
import heap_sort


def read_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def main():
    while True:
        print("\n============== MAIN MENU ==============")
        print("--- Data Structures ---")
        print("1. Stack")
        print("2. Queue")
        print("3. Singly Linked List")
        print("4. Doubly Linked List")
        print("5. Binary Tree")
        print("6. Binary Search Tree")
        print("--- Sorting ---")
        print("7. Bubble Sort")
        print("8. Insertion Sort")
        print("9. Merge Sort")
        print("10. Quick Sort")
        print("11. Heap Sort")
        print("0. Exit")
        choice = read_int("Enter choice: ")

        if choice == 1:
            stack.menu()
        elif choice == 2:
            queue_ll.menu()
        elif choice == 3:
            linked_list.menu()
        elif choice == 4:
            doubly_linked_list.menu()
        elif choice == 5:
            tree.menu()
        elif choice == 6:
            bst.menu()
        elif choice == 7:
            bubble_sort.menu()
        elif choice == 8:
            insertion_sort.menu()
        elif choice == 9:
            merge_sort.menu()
        elif choice == 10:
            quick_sort.menu()
        elif choice == 11:
            heap_sort.menu()
        elif choice == 0:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
