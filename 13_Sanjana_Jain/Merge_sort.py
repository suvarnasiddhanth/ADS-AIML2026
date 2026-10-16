import time

class Merge_sort:
    def __init__(self):
        pass

    def partition(self, A, l, h):
        if l < h:
            mid = (l + h) // 2

            # Sort the left half
            self.partition(A, l, mid)

            # Sort the right half
            self.partition(A, mid + 1, h)

    
            self.merge(A, l, mid, h)

    def merge(self, A, l, mid, h):
        left = A[l:mid + 1]
        right = A[mid + 1:h + 1]

        i = 0
        j = 0
        k = l

        # Compare elements from both halves
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                A[k] = left[i]
                i += 1
            else:
                A[k] = right[j]
                j += 1

            k += 1

        # Copy remaining elements from the left half
        while i < len(left):
            A[k] = left[i]
            i += 1
            k += 1

        # Copy remaining elements from the right half
        while j < len(right):
            A[k] = right[j]
            j += 1
            k += 1

    def sort(self, A):
        self.partition(A, 0, len(A) - 1)
        return A


b = Merge_sort()

numbers = [64, 34, 25, 12, 22, 11, 90]

print("Original list:", numbers)

start = time.time()
sorted_numbers = b.sort(numbers)
end = time.time()

time_taken = end - start

print("Sorted list:", sorted_numbers)
print("Time taken:", time_taken, "seconds")