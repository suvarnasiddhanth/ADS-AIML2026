def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(values):
    if len(values) <= 1:
        return values
    middle = len(values) // 2
    left = merge_sort(values[:middle])
    right = merge_sort(values[middle:])
    return merge(left, right)

def main():
    n = int(input("Enter n: "))
    arr = list(map(int, input(f"Enter {n} numbers: ").split()))

    print("Sorted:", merge_sort(arr))


if __name__ == "__main__":
    main()