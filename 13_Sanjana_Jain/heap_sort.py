import time

class Heap_sort:
    def __init__(self):
        pass

    def heapify(self, A, n, i):
        l = i
        left = 2*i+1
        right = 2*i+2

        if left<n and A[left]> A[l]:
            l = left

        if right <n and A[right]> A[l]:
            l = right

        if l!=i:
            A[i],A[l]=A[l],A[i]
            self.heapify(A,n,l)


    def sort(self, A):
        n = len(A)

        for i in range(n//2-1,-1,-1):
            self.heapify(A,n,i)

        for i in range(n-1,0,-1):
            A[i],A[0]=A[0],A[i]
            self.heapify(A,i,0)

        return A


b = Heap_sort()

numbers = [64, 34, 25, 12, 22, 11, 90]

print("Original list:", numbers)

start = time.time()
sorted_numbers = b.sort(numbers)
end = time.time()

time_taken = end - start

print("Sorted list:", sorted_numbers)
print("Time taken:", time_taken, "seconds")