class LinearSearch:
    def __init__(self, arr):
        self.arr = arr

    def search(self, target):
        for i in range(len(self.arr)):
            if self.arr[i] == target:
                return i
        return -1


def main():
    array = [5, 8, 9, 30]
    search = LinearSearch(array)

    while True:
        print("\n--- Linear Search Menu ---")
        print("1. Search for an element")
        print("2. Display the array")
        print("3. Change the array")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            try:
                target = int(input("Enter the element to find: "))
                found = search.search(target)

                if found == -1:
                    print("The element is not present in the array.")
                else:
                    print("The element is present at index:", found)
            except ValueError:
                print("Please enter a valid integer.")

        elif choice == "2":
            print("Current array:", search.arr)

        elif choice == "3":
            raw_values = input("Enter integers separated by spaces: ").strip()
            try:
                values = [int(item) for item in raw_values.split()]
                if not values:
                    print("Please enter at least one integer.")
                else:
                    search = LinearSearch(values)
                    print("Array updated.")
            except ValueError:
                print("Invalid input. Enter integers separated by spaces.")

        elif choice == "4":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Select an option from 1 to 4.")


if __name__ == "__main__":
    main()