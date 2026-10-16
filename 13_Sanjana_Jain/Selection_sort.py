import time
class Selection_sort:
    def __init__(self):
        pass

    def sort(self,A):
        n=len(A)
        for i in range(0,n-1):
            min = i
            for j in range(i+1,n):
                if A[j] < A[min]:
                    min = j
            if min!=i:
                t = A[i]
                A[i]=A[min]
                A[min]=t
        return A

b = Selection_sort()

numbers = [64, 34, 25, 12, 22, 11, 90]

print("Original list:", numbers)
start = time.time()
sorted_numbers = b.sort(numbers)
end = time.time()
time_taken = end-start
print("Sorted list:", sorted_numbers)
print("Time taken:",time_taken)