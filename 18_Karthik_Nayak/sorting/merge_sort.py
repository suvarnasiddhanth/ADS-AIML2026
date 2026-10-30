class MergeSort:
    def __init__(self, arr):
        self.arr = arr

    def merge_sort(self, values):
        if len(values) <= 1:
            return values

        mid = len(values) // 2
        left_half = self.merge_sort(values[:mid])
        right_half = self.merge_sort(values[mid:])

        return self.merge(left_half, right_half)

    def merge(self, left, right):
        result = []
        i = 0
        j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def sort(self):
        self.arr = self.merge_sort(self.arr)
        return self.arr


def main():
    sorter = MergeSort([4, 9, 10, 0, 6, 8])

    while True:
        print("\n--- Merge Sort Menu ---")
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
                    sorter = MergeSort(values)
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
