
def selection_sort(array):
    n = len(array)

    for i in range(n):
        min = i

        for j in range(i + 1, n):
            if array[j] < array[min]:
                min = j

        array[i], array[min] = array[min], array[i]

    return array
array = []

while True:
    print("\n----- SELECTION SORT MENU -----")
    print("1. Enter Array")
    print("2. Sort Array")
    print("3. Display Array")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        array = list(map(int, input("Enter array elements separated by spaces: ").split()))
        print("Array entered successfully.")

    elif choice == '2':
        if len(array) == 0:
            print("Array is empty! Enter elements first.")
        else:
            selection_sort(array)
            print("Sorted Array:", array)

    elif choice == '3':
        if len(array) == 0:
            print("Array is empty!")
        else:
            print("Array:", array)

    elif choice == '4':
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")
