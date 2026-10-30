def heapify(values, heap_size, root):
    largest = root
    left = 2*root + 1
    right = 2*root + 2

    if left < heap_size and values[left] > values[largest]:
        largest = left
    if right < heap_size and values[right] > values[largest]:
        largest = right

    if largest != root:
        values[root], values[largest] = values[largest], values[root]
        heapify(values, heap_size, largest)

def build_max_heap(values):
    n = len(values)
    for root in range( n // 2 -1, -1, -1):
        heapify(values, n, root)

def heap_sort(values):
    values = values.copy()
    n = len(values)
    build_max_heap(values)
    for end in range(n-1, 0, -1):
        values[0], values[end] = values[end], values[0]
        heapify(values, end, 0)
    return values

def main():
    n = int(input("Enter n: "))
    arr = list(map(int, input(f"Enter {n} numbers: ").split()))

    print("Sorted:", heap_sort(arr))


if __name__ == "__main__":
    main()