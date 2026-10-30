class SelectionSort:
    def __init__(self, arr):
        self.arr = arr

    def selection_sort(self):
        n = len(self.arr)

        for i in range(n):
            min_index = i

            for j in range(i + 1, n):
                if self.arr[j] < self.arr[min_index]:
                    min_index = j

            self.arr[i], self.arr[min_index] = self.arr[min_index], self.arr[i]

        return self.arr


def main():
    sorter = SelectionSort([2, 6, 8, 4, 1, 0, 9])

    while True:
        print("\n--- Selection Sort Menu ---")
        print("1. Display array")
        print("2. Sort array")
        print("3. Enter a new array")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            print("Current array:", sorter.arr)

        elif choice == "2":
            sorter.selection_sort()
            print("Sorted array:", sorter.arr)

        elif choice == "3":
            raw_values = input("Enter integers separated by spaces: ").strip()

            try:
                values = [int(item) for item in raw_values.split()]
                if not values:
                    print("Please enter at least one number.")
                else:
                    sorter = SelectionSort(values)
                    print("New array saved:", sorter.arr)
            except ValueError:
                print("Invalid input. Enter integers separated by spaces.")

        elif choice == "4":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Select an option from 1 to 4.")


if __name__ == "__main__":
    main()