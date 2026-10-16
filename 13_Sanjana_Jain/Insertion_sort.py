import time
class Insertion_sort:
    def __init__(self):
        pass

    def sort(self,A):
        n=len(A)
        for i in range(1,n):
            key = A[i]
            j=i-1
            while j>=0 and A[j]>key:
                A[j+1] = A[j]
                j=j-1
            A[j + 1] = key
        return A

b = Insertion_sort()

numbers = [64, 34, 25, 12, 22, 11, 90]

print("Original list:", numbers)
start = time.time()
sorted_numbers = b.sort(numbers)
end = time.time()
time_taken = end-start
print("Sorted list:", sorted_numbers)
print("Time taken:",time_taken)