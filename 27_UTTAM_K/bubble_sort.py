"""
Bubble Sort

Compare neighbours and swap them if they are in the wrong order. After each
pass the largest remaining value has "bubbled" to the end. If a pass makes
no swaps, the list is already sorted, so we stop early.

Run on its own:     python bubble_sort.py
Or from main menu:  python main.py
"""


# Bubble Sort    Best O(n), Avg/Worst O(n^2), Space O(1), stable
def bubble_sort(values):
    n = len(values)
    for end in range(n - 1, 0, -1):
        swapped = False
        for i in range(end):
            if values[i] > values[i + 1]:
                values[i], values[i + 1] = values[i + 1], values[i]
                swapped = True
        if not swapped:
            break
    return values


# ---------------------------------------------------------------------
# Step-by-step version: same algorithm with prints and counters added.
# For display only. In the exam you write bubble_sort() above.
# ---------------------------------------------------------------------
def bubble_sort_steps(values):
    n = len(values)
    comparisons = swaps = 0
    print("Start   :", values)
    for end in range(n - 1, 0, -1):
        swapped = False
        for i in range(end):
            comparisons += 1
            if values[i] > values[i + 1]:
                values[i], values[i + 1] = values[i + 1], values[i]
                swapped = True
                swaps += 1
        print("Pass", n - end, " :", values[:end], "|", values[end:], "  <- right side is in final place")
        if not swapped:
            print("No swaps in this pass, so the list is sorted. Stopping early.")
            break
    print("Sorted  :", values)
    print("Comparisons:", comparisons, "  Swaps:", swaps)
    return values


COMPLEXITY = """Bubble Sort
  Best case   : O(n)    already sorted, stops after one pass with no swaps
  Average     : O(n^2)
  Worst case  : O(n^2)  reverse sorted
  Extra space : O(1)    sorts in place
  Stable      : Yes     equal values keep their order"""


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
        print("\n------ BUBBLE SORT ------")
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
            print("Sorted  :", bubble_sort(numbers[:]))     # sort a copy, keep the original
        elif choice == 3:
            bubble_sort_steps(numbers[:])
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
