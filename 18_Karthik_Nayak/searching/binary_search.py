class BinarySearch:
    def __init__(self):
        self.arr = []

    def bin_search(self, target):
        low = 0
        high = len(self.arr) - 1

        while low <= high:
            mid = (low + high) // 2

            if self.arr[mid] == target:
                return mid
            elif target < self.arr[mid]:
                high = mid - 1
            else:
                low = mid + 1

        return None


def main():
    searcher = BinarySearch()

    while True:
        print("\n--- Binary Search Menu ---")
        print("1. Enter a sorted array")
        print("2. Search for a value")
        print("3. Display the array")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            raw_values = input("Enter sorted integers separated by spaces: ").strip()

            try:
                numbers = [int(item) for item in raw_values.split()]
                if not numbers:
                    print("Please enter at least one number.")
                elif numbers != sorted(numbers):
                    print("The array must be sorted in ascending order.")
                else:
                    searcher.arr = numbers
                    print("Array saved.")
            except ValueError:
                print("Invalid input. Enter integers separated by spaces.")

        elif choice == "2":
            if not searcher.arr:
                print("Enter a sorted array first.")
                continue

            try:
                target = int(input("Enter the value to search for: "))
                position = searcher.bin_search(target)

                if position is not None:
                    print("Target found at index:", position)
                else:
                    print("The target is not present in the array.")
            except ValueError:
                print("Please enter a valid integer.")

        elif choice == "3":
            if searcher.arr:
                print("Current array:", searcher.arr)
            else:
                print("No array has been entered yet.")

        elif choice == "4":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Select an option from 1 to 4.")


if __name__ == "__main__":
    main()