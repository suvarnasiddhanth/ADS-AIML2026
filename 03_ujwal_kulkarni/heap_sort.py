def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    # Build max heap
    for i in range((n // 2) - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements from heap
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
arr = []

while True:
    print("\n----- HEAP SORT MENU -----")
    print("1. Enter Array")
    print("2. Heap Sort")
    print("3. Display Array")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        arr = list(map(int, input(
            "Enter array elements separated by spaces: "
        ).split()))
        print("Array entered successfully.")

    elif choice == '2':
        if len(arr) == 0:
            print("Array is empty! Enter elements first.")
        else:
            heap_sort(arr)
            print("Sorted Array:", arr)

    elif choice == '3':
        if len(arr) == 0:
            print("Array is empty!")
        else:
            print("Array:", arr)

    elif choice == '4':
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")
