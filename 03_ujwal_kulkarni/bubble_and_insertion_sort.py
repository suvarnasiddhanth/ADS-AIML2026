def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        swapped = False

        for j in range(n - i - 1):
            if arr[j + 1] < arr[j]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
                swapped = True

        if swapped == False:
            break

    return arr


def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        j = i - 1
        key = arr[i]

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j = j - 1

        arr[j + 1] = key

    return arr


arr = []

while True:
    print("\n----- SORTING MENU -----")
    print("1. Enter Array")
    print("2. Bubble Sort")
    print("3. Insertion Sort")
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
            arr = bubble_sort(arr)
            print("Array after Bubble Sort:", arr)

    elif choice == '3':
        if len(arr) == 0:
            print("Array is empty! Enter elements first.")
        else:
            arr = insertion_sort(arr)
            print("Array after Insertion Sort:", arr)

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
