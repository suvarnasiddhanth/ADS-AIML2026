def max_heapify(arr, n, i):
    largest = i
    left = 2*i+1
    right = 2*i+2
    if left<n and arr[left]>arr[largest]:
        largest = left
    if right<n and arr[right]>arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)

def build_max_heap(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, n, i)

def heap_sort(arr):
    n = len(arr)
    build_max_heap(arr)
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        max_heapify(arr,i,0)
    return arr

def heap_sort_menu():

    arr = list(map(int, input("Enter elements: ").split()))

    while True:
        print("\n--- HEAP SORT ---")
        print("1. Display")
        print("2. Sort")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            print("Array:", arr)

        elif choice == "2":
            arr = heap_sort(arr)
            print("Sorted:", arr)

        elif choice == "3":
            print("Exiting program.")
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    heap_sort_menu()