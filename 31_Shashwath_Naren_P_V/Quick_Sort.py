def partition(values, low, high):
    pivot = values[high]
    i = low - 1
    for j in range(low, high):
        if values[j] <= pivot:
            i += 1
            values[i], values[j] = values[j], values[i]
    values[i+1], values[high] = values[high], values[i + 1]
    return i + 1

def quick_sort(values, low = 0, high = None):
    values = values.copy() if high is None and low == 0 else values
    if high is None:
        high = len(values) - 1
    if low<high:
        pivot_index = partition(values, low,high)
        quick_sort(values, low, pivot_index-1)
        quick_sort(values, pivot_index + 1, high)
    return values

def main():
    n = int(input("Enter n: "))
    arr = list(map(int, input(f"Enter {n} numbers: ").split()))

    print("Sorted:", quick_sort(arr))


if __name__ == "__main__":
    main()