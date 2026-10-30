def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def selection_sort_menu():

    arr = list(map(int, input("\n Enter the elements of the array: ").split()))

    while True:
        print("\n1. Display")
        print("2. Sort")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            print(arr)
        elif choice == "2":
            arr = selection_sort(arr)
            print("Sorted:", arr)
        elif choice == "3":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    selection_sort_menu()