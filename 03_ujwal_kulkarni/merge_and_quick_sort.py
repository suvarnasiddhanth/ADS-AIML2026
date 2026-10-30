def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)

        quick_sort(arr, low, p - 1)
        quick_sort(arr, p + 1, high)


def merge(arr, low, mid, high):
    left = arr[low:mid + 1]
    right = arr[mid + 1:high + 1]

    i = 0
    j = 0
    k = low

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


def merge_sort(arr, low, high):
    if low < high:
        mid = (low + high) // 2

        merge_sort(arr, low, mid)
        merge_sort(arr, mid + 1, high)

        merge(arr, low, mid, high)
arr = []

while True:
    print("\n----- SORTING MENU -----")
    print("1. Enter Array")
    print("2. Quick Sort")
    print("3. Merge Sort")
    print("4. Display Array")
    print("5. Exit")

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
            quick_sort(arr, 0, len(arr) - 1)
            print("Array after Quick Sort:", arr)

    elif choice == '3':
        if len(arr) == 0:
            print("Array is empty! Enter elements first.")
        else:
            merge_sort(arr, 0, len(arr) - 1)
            print("Array after Merge Sort:", arr)

    elif choice == '4':
        if len(arr) == 0:
            print("Array is empty!")
        else:
            print("Array:", arr)

    elif choice == '5':
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")
