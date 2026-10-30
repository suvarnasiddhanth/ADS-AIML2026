def insertion_sort(arr):
    n = len(arr)
    for i in range(1,n):
        key = arr[i]
        j = i-1
        # Shift larger elements to the right
        while j>=0 and arr[j]>key:
            arr[j+1] = arr[j]
            j=j-1
        # Insert key in the correct position
        arr[j+1] = key
    return arr

def insertion_sort_menu():

    arr = list(map(int, input("\n Enter the elements of the array: ").split()))

    while True:
        print("\n1. Display")
        print("2. Sort")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            print(arr)
        elif choice == "2":
            arr = insertion_sort(arr)
            print("Sorted:", arr)
        elif choice == "3":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    insertion_sort_menu()