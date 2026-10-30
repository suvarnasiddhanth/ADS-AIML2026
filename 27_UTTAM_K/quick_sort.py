"""
Quick Sort (Lomuto partition, pivot = last element)

Divide and conquer: pick a pivot and partition the list so everything
<= pivot is on its left and everything bigger is on its right. The pivot
is now in its final place. Then quick sort the left part and the right part.

Run on its own:     python quick_sort.py
Or from main menu:  python main.py
"""


# Partition (Lomuto scheme, pivot = last element)
def partition(values, low, high):
    pivot = values[high]
    i = low - 1                         # end of the "<= pivot" zone
    for j in range(low, high):
        if values[j] <= pivot:
            i += 1
            values[i], values[j] = values[j], values[i]
    values[i + 1], values[high] = values[high], values[i + 1]   # pivot to its final place
    return i + 1


# Quick Sort    Avg O(n log n), Worst O(n^2), Space O(log n), not stable
def quick_sort(values, low=0, high=None):
    if high is None:
        high = len(values) - 1
    if low < high:
        pivot_index = partition(values, low, high)
        quick_sort(values, low, pivot_index - 1)
        quick_sort(values, pivot_index + 1, high)
    return values


# ---------------------------------------------------------------------
# Step-by-step version: same algorithm with prints and a counter added.
# For display only. In the exam you write partition() and quick_sort() above.
# Indentation shows the depth of the recursion.
# ---------------------------------------------------------------------
comparisons = 0


def quick_sort_steps(values, low=0, high=None, depth=0):
    global comparisons
    if high is None:
        high = len(values) - 1
    if depth == 0:
        comparisons = 0
        print("Start :", values)
    if low < high:
        pad = "    " * depth
        part = values[low:high + 1]
        comparisons += high - low       # partition compares every item except the pivot once
        pivot_index = partition(values, low, high)
        print(pad + "partition", part, "pivot =", values[pivot_index], "->",
              values[low:pivot_index], "[" + str(values[pivot_index]) + "]",
              values[pivot_index + 1:high + 1])
        quick_sort_steps(values, low, pivot_index - 1, depth + 1)
        quick_sort_steps(values, pivot_index + 1, high, depth + 1)
    if depth == 0:
        print("Sorted:", values)
        print("Comparisons:", comparisons)
    return values


COMPLEXITY = """Quick Sort
  Best case   : O(n log n)  pivot splits the list in half each time
  Average     : O(n log n)
  Worst case  : O(n^2)      pivot is always the smallest or largest,
                            e.g. an ALREADY SORTED list with last-element pivot
  Extra space : O(log n)    recursion stack (O(n) in the worst case), sorts in place
  Stable      : No          long-distance swaps can reorder equal values"""


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
        print("\n------ QUICK SORT ------")
        print("1. Enter numbers")
        print("2. Sort")
        print("3. Sort step by step")
        print("4. Display entered numbers")
        print("5. Time and space complexity")
        print("0. Back")
        choice = read_int("Enter choice: ")

        if choice in (2, 3, 4) and not numbers:
            print("No numbers yet. Choose 1 to enter some.")
        elif choice == 1:
            numbers = read_int_list("Enter numbers separated by spaces: ")
            if numbers:
                print("Entered:", numbers)
            else:
                print("No numbers entered.")
        elif choice == 2:
            print("Original:", numbers)
            print("Sorted  :", quick_sort(numbers[:]))      # sort a copy, keep the original
        elif choice == 3:
            quick_sort_steps(numbers[:])
        elif choice == 4:
            print("Numbers:", numbers)
        elif choice == 5:
            print(COMPLEXITY)
        elif choice == 0:
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    menu()
