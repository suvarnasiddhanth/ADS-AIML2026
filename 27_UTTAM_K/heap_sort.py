"""
Heap Sort

1. Build a MAX-HEAP: every parent >= its children, so the largest value
   is at index 0. (Stored as an array: children of i are 2i+1 and 2i+2.)
2. Swap the root (the max) with the last item of the heap, shrink the heap
   by one, and heapify the root to repair it. Repeat.

Run on its own:     python heap_sort.py
Or from main menu:  python main.py
"""


# Heapify: repair one subtree by sifting the root down      O(log n)
def heapify(values, heap_size, root):
    largest = root
    left_child = 2 * root + 1
    right_child = 2 * root + 2
    if left_child < heap_size and values[left_child] > values[largest]:
        largest = left_child
    if right_child < heap_size and values[right_child] > values[largest]:
        largest = right_child
    if largest != root:
        values[root], values[largest] = values[largest], values[root]
        heapify(values, heap_size, largest)


# Build max heap: heapify every non-leaf, last one first     O(n)
def build_max_heap(values):
    n = len(values)
    for root in range(n // 2 - 1, -1, -1):
        heapify(values, n, root)


# Heap Sort    O(n log n) always, Space O(1), not stable
def heap_sort(values):
    n = len(values)
    for root in range(n // 2 - 1, -1, -1):      # phase 1: build max heap
        heapify(values, n, root)
    for end in range(n - 1, 0, -1):             # phase 2: move max to the end, repair
        values[0], values[end] = values[end], values[0]
        heapify(values, end, 0)
    return values


# ---------------------------------------------------------------------
# Step-by-step version: uses the same heapify, with prints added.
# For display only. In the exam you write the three functions above.
# ---------------------------------------------------------------------
def print_heap(values, size, i=0, level=0):
    """Print heap values[0:size] as a sideways tree (right child on top)."""
    if i < size:
        print_heap(values, size, 2 * i + 2, level + 1)
        print("      " * level + str(values[i]))
        print_heap(values, size, 2 * i + 1, level + 1)


def heap_sort_steps(values):
    n = len(values)
    print("Start:", values)
    print("\nPhase 1: build the max heap (heapify from index", n // 2 - 1, "down to 0)")
    for root in range(n // 2 - 1, -1, -1):
        heapify(values, n, root)
        print("  heapify(root=" + str(root) + ") ->", values)
    print("Max heap (sideways tree, right child on top):")
    print_heap(values, n)
    print("\nPhase 2: swap the max to the end, then heapify the smaller heap")
    for end in range(n - 1, 0, -1):
        values[0], values[end] = values[end], values[0]
        heapify(values, end, 0)
        print("  move", values[end], "to index", end, "-> heap", values[:end], "| sorted", values[end:])
    print("Sorted:", values)
    return values


COMPLEXITY = """Heap Sort
  Best case   : O(n log n)
  Average     : O(n log n)
  Worst case  : O(n log n)  same every time
  Build heap  : O(n)
  Extra space : O(1)        sorts in place (recursive heapify uses O(log n) stack)
  Stable      : No"""


# ---------------------------------------------------------------------
# Menu
# ---------------------------------------------------------------------
def read_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def read_int_list(prompt):
    while True:
        try:
            return [int(x) for x in input(prompt).split()]
        except ValueError:
            print("Invalid input. Enter whole numbers separated by spaces.")


numbers = []        # kept here, so the list stays when you go back to the main menu


def menu():
    global numbers
    while True:
        print("\n------ HEAP SORT ------")
        print("1. Enter numbers")
        print("2. Sort")
        print("3. Sort step by step")
        print("4. Build max heap only")
        print("5. Display entered numbers")
        print("6. Time and space complexity")
        print("0. Back")
        choice = read_int("Enter choice: ")

        if choice in (2, 3, 4, 5) and not numbers:
            print("No numbers yet. Choose 1 to enter some.")
        elif choice == 1:
            numbers = read_int_list("Enter numbers separated by spaces: ")
            if numbers:
                print("Entered:", numbers)
            else:
                print("No numbers entered.")
        elif choice == 2:
            print("Original:", numbers)
            print("Sorted  :", heap_sort(numbers[:]))       # sort a copy, keep the original
        elif choice == 3:
            heap_sort_steps(numbers[:])
        elif choice == 4:
            heap = numbers[:]
            build_max_heap(heap)
            print("Max heap as array:", heap)
            print("As a tree (sideways, right child on top):")
            print_heap(heap, len(heap))
        elif choice == 5:
            print("Numbers:", numbers)
        elif choice == 6:
            print(COMPLEXITY)
        elif choice == 0:
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    menu()
