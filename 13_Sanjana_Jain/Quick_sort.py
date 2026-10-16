import time

class Quick_sort:
    def __init__(self):
        pass

    def partition(self, A, l, h):
        if l < h:
            pivot = self.quick_partition(A,l,h)

            # Sort the left half
            self.partition(A, l, pivot-1)

            # Sort the right half
            self.partition(A, pivot+1 + 1, h)


    def quick_partition(self, A, l, h):
        pivot = A[h]
        i = l-1
        for j in range(l,h):
            if A[j]<= pivot:
                i+=1
                A[i],A[j]= A[j],A[i]
        A[i+1],A[h] = A[h],A[i+1]
        return i+1       


    def sort(self, A):
        self.partition(A, 0, len(A) - 1)
        return A


b = Quick_sort()

numbers = [64, 34, 25, 12, 22, 11, 90]

print("Original list:", numbers)

start = time.time()
sorted_numbers = b.sort(numbers)
end = time.time()

time_taken = end - start

print("Sorted list:", sorted_numbers)
print("Time taken:", time_taken, "seconds")