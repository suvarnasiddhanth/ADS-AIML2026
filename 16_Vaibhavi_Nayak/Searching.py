# Linear Search
def LinearSearch(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1


# Binary Search
def BinarySearch(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid
        elif key < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return -1


arr = [10, 20, 30, 40, 50, 60, 70]
key = 40

print("Array:", arr)
print("Element to search:", key)

result1 = LinearSearch(arr, key)

if result1 != -1:
    print("Linear Search: Element found at index", result1)
else:
    print("Linear Search: Element not found")

result2 = BinarySearch(arr, key)

if result2 != -1:
    print("Binary Search: Element found at index", result2)
else:
    print("Binary Search: Element not found")