class HeapSort:
    def __init__(self, arr):
        self.arr = arr

    def heapify(self, size, root_index):
        largest = root_index
        left = 2 * root_index + 1
        right = 2 * root_index + 2

        if left < size and self.arr[left] > self.arr[largest]:
            largest = left

        if right < size and self.arr[right] > self.arr[largest]:
            largest = right

        if largest != root_index:
            self.arr[root_index], self.arr[largest] = (
                self.arr[largest],
                self.arr[root_index],
            )
            self.heapify(size, largest)

    def heap_sort(self):
        size = len(self.arr)

        # Build a max heap
        for index in range(size // 2 - 1, -1, -1):
            self.heapify(size, index)

        # Move the largest item to the end one at a time
        for end in range(size - 1, 0, -1):
            self.arr[0], self.arr[end] = self.arr[end], self.arr[0]
            self.heapify(end, 0)

        return self.arr


def main():
    sorter = HeapSort([4, 9, 10, 0, 6, 8])

    while True:
        print("\n--- Heap Sort Menu ---")
        print("1. Display array")
        print("2. Sort array")
        print("3. Enter a new array")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            print("Current array:", sorter.arr)

        elif choice == "2":
            sorter.heap_sort()
            print("Sorted array:", sorter.arr)

        elif choice == "3":
            raw_values = input("Enter integers separated by spaces: ").strip()

            try:
                values = [int(item) for item in raw_values.split()]
                if not values:
                    print("Please enter at least one number.")
                else:
                    sorter = HeapSort(values)
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