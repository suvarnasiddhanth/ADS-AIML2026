def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if swapped == False:
            
            break
    return arr

def bubble_sort_menu():

    arr = list(map(int, input("\n Enter the elements of the array: ").split()))

    while True:
        print("\n1. Display")
        print("2. Sort")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            print(arr)
        elif choice == "2":
            arr = bubble_sort(arr)
            print("Sorted:", arr)
        elif choice == "3":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    bubble_sort_menu()