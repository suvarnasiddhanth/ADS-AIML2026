def binary_search(values, target):
    low = 0 
    high = len(values) - 1

    while low <= high:
        middle = (low+high) // 2
        if values[middle] == target:
            return middle
        elif target < values[middle]:
            high = middle - 1
        else:
            low = middle + 1
    return -1

def main():
    n = int(input("Enter n: "))
    arr = list(map(int, input(f"Enter {n} sorted numbers: ").split()))
    target = int(input("Enter target to search: "))

    result = binary_search(arr, target)

    if result != -1:
        print(f"Found {target} at index {result}")
    else:
        print(f"{target} not found")


if __name__ == "__main__":
    main()