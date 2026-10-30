def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        swapped = False

        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def main():
    n = int(input("Enter n: "))
    arr = list(map(int, input(f"Enter {n} numbers: ").split()))

    print("Sorted:", bubble_sort(arr))


if __name__ == "__main__":
    main()