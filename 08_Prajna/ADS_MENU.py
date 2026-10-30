from Singly_Linked_list import singly_linked_list_menu
from Doubly_Linked_list import doubly_linked_list_menu

from Stack_1_using_array import stack_array_menu
from Stack_2_using_linkedlist import stack_linked_list_menu

from Queue_1_using_array import queue_array_menu
from Queue_2_using_linkedlist import queue_linked_list_menu
from Queue_3_circular import queue_circular_menu
from Queue_4_Flexible_queue import flexible_queue_menu

from Searching_1_linear_search import linear_search_menu
from Searching_2_binary_search import binary_search_menu

from Sorting_1_bubble_sort import bubble_sort_menu
from Sorting_2_selection_sort import selection_sort_menu
from Sorting_3_insertion_sort import insertion_sort_menu
from Sorting_4_merge_sort import merge_sort_menu
from Sorting_5_quick_sort import quick_sort_menu
from Sorting_6_heap_sort import heap_sort_menu

from Trees import trees_menu

def stack_menu():
    while True:
        print("\n========== STACK MENU ==========")
        print("1. Stack using Array")
        print("2. Stack using Linked List")
        print("3. Back to Main Menu")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            stack_array_menu()
        elif choice == "2":
            stack_linked_list_menu()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

def queue_menu():
    while True:
        print("\n========== QUEUE MENU ==========")
        print("1. Queue using Array")
        print("2. Queue using Linked List")
        print("3. Circular Queue")
        print("4. Back to Main Menu")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            queue_array_menu()
        elif choice == "2":
            queue_linked_list_menu()
        elif choice == "3":
            queue_circular_menu()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

def searching_menu():
    while True:
        print("\n========== SEARCHING MENU ==========")
        print("1. Linear Search")
        print("2. Binary Search")
        print("3. Back to Main Menu")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            linear_search_menu()
        elif choice == "2":
            binary_search_menu()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

def sorting_menu():
    while True:
        print("\n========== SORTING MENU ==========")
        print("1. Bubble Sort")
        print("2. Selection Sort")
        print("3. Insertion Sort")
        print("4. Merge Sort")
        print("5. Quick Sort")
        print("6. Heap Sort")
        print("7. Back to Main Menu")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            bubble_sort_menu()
        elif choice == "2":
            selection_sort_menu()
        elif choice == "3":
            insertion_sort_menu()
        elif choice == "4":
            merge_sort_menu()
        elif choice == "5":
            quick_sort_menu()
        elif choice == "6":
            heap_sort_menu()
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please try again.")

def main_menu():
    while True:
        print("\n========== ADS LAB MENU ==========")
        print("1. Singly Linked List (SL)")
        print("2. Doubly Linked List (DL)")
        print("3. Stack")
        print("4. Queue")
        print("5. Flexible Queue")
        print("6. Searching")
        print("7. Sorting")
        print("8. Trees")
        print("9. Exit")

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
            searching_menu()
        elif choice == "7":
            sorting_menu()
        elif choice == "8":
            trees_menu()
        elif choice == "9":
            print("Exiting.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()