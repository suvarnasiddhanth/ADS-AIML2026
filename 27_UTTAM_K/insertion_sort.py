"""
Insertion Sort

Like sorting playing cards in your hand: take the next value (the "key"),
shift every bigger value in the sorted part one place right, and drop the
key into the gap.

Run on its own:     python insertion_sort.py
Or from main menu:  python main.py
"""


# Insertion Sort    Best O(n), Avg/Worst O(n^2), Space O(1), stable
def insertion_sort(values):
    for i in range(1, len(values)):
        key = values[i]
        j = i - 1
        while j >= 0 and values[j] > key:
            values[j + 1] = values[j]
            j -= 1
        values[j + 1] = key
    return values


# ---------------------------------------------------------------------
# Step-by-step version: same algorithm with prints and counters added.
# For display only. In the exam you write insertion_sort() above.
# ---------------------------------------------------------------------
def insertion_sort_steps(values):
    comparisons = shifts = 0
    print("Start :", values)
    for i in range(1, len(values)):
        key = values[i]
        j = i - 1
        moved = []
        while j >= 0:
            comparisons += 1
            if values[j] <= key:
                break
            values[j + 1] = values[j]
            moved.append(values[j])
            shifts += 1
            j -= 1
        values[j + 1] = key
        print("key =", key, " :", values[:i + 1], "|", values[i + 1:],
              "  shifted", moved, "right, key placed at index", j + 1)
    print("Sorted:", values)
    print("Comparisons:", comparisons, "  Shifts:", shifts)
    return values


COMPLEXITY = """Insertion Sort
  Best case   : O(n)    already sorted, nothing to shift
  Average     : O(n^2)
  Worst case  : O(n^2)  reverse sorted, every key shifts all the way left
  Extra space : O(1)    sorts in place
  Stable      : Yes     equal values keep their order
  Good for    : small or nearly sorted lists"""


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
        print("\n------ INSERTION SORT ------")
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
            print("Sorted  :", insertion_sort(numbers[:]))  # sort a copy, keep the original
        elif choice == 3:
            insertion_sort_steps(numbers[:])
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
