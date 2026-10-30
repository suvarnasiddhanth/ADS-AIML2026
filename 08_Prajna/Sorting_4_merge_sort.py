def merge(arr, left, mid, right):
    L = arr[left:mid+1]
    R = arr[mid+1:right+1]
    i=0
    j=0
    k=left
    while i<len(L) and j<len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i=i+1
        else:
            arr[k] = R[j]
            j=j+1
        k=k+1

    while i<len(L):
        arr[k] = L[i]
        i=i+1
        k=k+1

    while i<len(R):
        arr[k] = R[j]
        j=j+1
        k=k+1

def merge_sort(arr, left, right):
    if left<right:
        mid = (left+right) // 2
        merge_sort(arr, left, mid) 
        merge_sort(arr, mid+1, right)
        merge(arr, left, mid, right)

def merge_sort_menu():

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
            merge_sort(arr, 0, len(arr) - 1)
            print("Sorted:", arr)

        elif choice == "3":
            print("Exiting program.")
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    merge_sort_menu()