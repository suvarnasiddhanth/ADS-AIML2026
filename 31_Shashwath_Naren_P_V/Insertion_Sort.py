def insertion_sort(arr):
    arr = arr.copy()
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >=0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

def main():
    n = int(input("Enter n: "))
    arr = list(map(int, input(f"Enter {n} numbers: ").split()))

    print("Sorted:", insertion_sort(arr))


if __name__ == "__main__":
    main()