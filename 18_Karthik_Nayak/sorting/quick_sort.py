class QuickSort:
    def __init__(self, arr):
        self.arr = arr

    def quick_sort(self, low, high):
        if low < high:
            pivot_pos = self.partition(low, high)
            self.quick_sort(low, pivot_pos - 1)
            self.quick_sort(pivot_pos + 1, high)

        return self.arr

    def partition(self, low, high):
        pivot = self.arr[high]
        boundary = low - 1

        for current in range(low, high):
            if self.arr[current] <= pivot:
                boundary += 1
                self.arr[boundary], self.arr[current] = (
                    self.arr[current],
                    self.arr[boundary],
                )

        self.arr[boundary + 1], self.arr[high] = (
            self.arr[high],
            self.arr[boundary + 1],
        )

        return boundary + 1


def main():
    sorter = QuickSort([4, 9, 10, 0, 6, 8])

    while True:
        print("\n--- Quick Sort Menu ---")
        print("1. Display array")
        print("2. Sort array")
        print("3. Enter a new array")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            print("Current array:", sorter.arr)

        elif choice == "2":
            sorter.quick_sort(0, len(sorter.arr) - 1)
            print("Sorted array:", sorter.arr)

        elif choice == "3":
            raw_values = input("Enter integers separated by spaces: ").strip()
            try:
                values = [int(item) for item in raw_values.split()]
                if not values:
                    print("Please enter at least one number.")
                else:
                    sorter = QuickSort(values)
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
