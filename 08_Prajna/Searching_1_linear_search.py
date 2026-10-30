def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def linear_search_menu():
    arr = list(map(int, input("Enter the elements: ").split()))

    while True:
        print("\n Linear Search")
        print("\n 1. Display the array")
        print("\n 2. Search for an element")
        print("\n 3. Exit")

        choice = input("\n Enter the choice:")

        if choice == "1":
            print("Array elements are:", arr)

        elif choice == "2":
            target = int(input("\n Enter the element to search:"))
            result = linear_search(arr, target)
            if result == -1:
                print(f"Element {target} not found in the array.")
            else:
                print("\n Element found at index: ", result)

        elif choice == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    linear_search_menu()