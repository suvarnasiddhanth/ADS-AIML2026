def linear_search(values, target):
    for index in range(len(values)):
        if values[index] == target:
            return index
    return -1

def main():
    n = int(input("Enter n : "))
    arr = list(map(int, input(f'Enter {n} numbers : ').split()))
    target = int(input("Enter target to search : "))

    result = linear_search(arr, target)

    if result != -1:
        print(f'Found {target} at index {result}')
    else:
        print(f"{target} not found")

if __name__ == "__main__":
    main()