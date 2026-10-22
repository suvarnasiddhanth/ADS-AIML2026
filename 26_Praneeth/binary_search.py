def binary_search(a, target):
    """Iterative. Array MUST be sorted."""
    low, high = 0, len(a) - 1
    while low <= high:
        mid = (low + high) // 2
        if a[mid] == target:
            return mid
        elif a[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
 
print(binary_search([23, 45, 69, 75], 23))