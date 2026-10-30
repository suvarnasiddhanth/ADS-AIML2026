def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def quick_sort(arr, low, high):
    if low<high:
        p = partition(arr, low, high)
        quick_sort(arr, low, p-1)
        quick_sort(arr, p+1, high)
    return arr

def quick_sort_menu():

    arr = list(map(int, input("Enter elements: ").split()))

    while True:
        print("\n--- MERGE SORT ---")
        print("1. Display")
        print("2. Sort")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            print("Array:", arr)

        elif choice == "2":
            quick_sort(arr, 0, len(arr) - 1)
            print("Sorted:", arr)

        elif choice == "3":
            print("Exiting program.")
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    quick_sort_menu()