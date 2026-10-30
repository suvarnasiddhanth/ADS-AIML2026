"""
Merge Sort

Divide and conquer: split the list in half, sort each half recursively,
then merge the two sorted halves. A list of 0 or 1 items is already sorted.

merge_sort returns a NEW sorted list (it does not sort in place).

Run on its own:     python merge_sort.py
Or from main menu:  python main.py
"""


# Merge two sorted lists into one sorted list
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:         # <= keeps it stable
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])             # leftovers (only one of these has any)
    result.extend(right[j:])
    return result


# Merge Sort    O(n log n) always, Space O(n), stable
def merge_sort(values):
    if len(values) <= 1:
        return values
    middle = len(values) // 2
    left_half = merge_sort(values[:middle])
    right_half = merge_sort(values[middle:])
    return merge(left_half, right_half)


# ---------------------------------------------------------------------
# Step-by-step version: same algorithm with prints and a counter added.
# For display only. In the exam you write merge() and merge_sort() above.
# Indentation shows the depth of the recursion.
# ---------------------------------------------------------------------
comparisons = 0


def merge_sort_steps(values, depth=0):
    global comparisons
    pad = "    " * depth
    if depth == 0:
        comparisons = 0
    if len(values) <= 1:
        print(pad + "base case", values)
        return values
    middle = len(values) // 2
    print(pad + "split", values, "->", values[:middle], "+", values[middle:])
    left_half = merge_sort_steps(values[:middle], depth + 1)
    right_half = merge_sort_steps(values[middle:], depth + 1)

    result = []
    i = j = 0
    while i < len(left_half) and j < len(right_half):
        comparisons += 1
        if left_half[i] <= right_half[j]:
            result.append(left_half[i])
            i += 1
        else:
            result.append(right_half[j])
            j += 1
    result.extend(left_half[i:])
    result.extend(right_half[j:])
    print(pad + "merge", left_half, "+", right_half, "->", result)

    if depth == 0:
        print("Sorted:", result)
        print("Comparisons:", comparisons)
    return result


COMPLEXITY = """Merge Sort
  Best case   : O(n log n)
  Average     : O(n log n)
  Worst case  : O(n log n)  same every time: log n levels, O(n) merging per level
  Extra space : O(n)        new lists are made while merging (not in place)
  Stable      : Yes         <= takes from the left half on ties"""


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
        print("\n------ MERGE SORT ------")
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
            print("Sorted  :", merge_sort(numbers[:]))
        elif choice == 3:
            merge_sort_steps(numbers[:])
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
