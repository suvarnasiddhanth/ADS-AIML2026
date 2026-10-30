def binary_search(arr, target):
    low = 0 
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif target > arr[mid]:
            low = mid + 1 #search right half
        else:
            high = mid - 1 #search left half

    return -1

def binary_search_menu():

    arr = list(map(int ,input("\n Enter the elements: ").split()))

    while True:
        print("\n Binary Search:")
        print("\n 1. Display the array")
        print("\n 2. Search for an element")
        print("\n 3. Exit")

        choice = input("\n Enter the choice: ")

        if choice == "1":
            print("Array elements are:", arr)

        elif choice == "2":
            target = int(input("\n Enter the element to search:"))
            result = binary_search(arr, target)
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
    binary_search_menu()