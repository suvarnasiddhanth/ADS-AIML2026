class BubbleSort:
    def __init__(self, arr):
        self.arr = arr

    def sort(self):
        n = len(self.arr)

        for i in range(n):
            for j in range(n - i - 1):
                if self.arr[j] > self.arr[j + 1]:
                    self.arr[j], self.arr[j + 1] = self.arr[j + 1], self.arr[j]

        return self.arr


def main():
    sorter = BubbleSort([2, 6, 9, 4, 0, 8])

    while True:
        print("\n--- Bubble Sort Menu ---")
        print("1. Display array")
        print("2. Sort array")
        print("3. Enter a new array")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            print("Current array:", sorter.arr)

        elif choice == "2":
            sorter.sort()
            print("Sorted array:", sorter.arr)

        elif choice == "3":
            raw_values = input("Enter integers separated by spaces: ").strip()
            try:
                values = [int(item) for item in raw_values.split()]
                if not values:
                    print("Please enter at least one number.")
                else:
                    sorter = BubbleSort(values)
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