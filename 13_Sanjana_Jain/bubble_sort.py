import time
class Bubble_sort:
    def __init__(self):
        pass

    def sort(self,A):
        n=len(A)
        for i in range(n):
            for j in range(n-i-1):
                if A[j+1]<A[j]:
                    t = A[j]
                    A[j]=A[j+1]
                    A[j+1]=t
        return A

b = Bubble_sort()

numbers = [64, 34, 25, 12, 22, 11, 90]

print("Original list:", numbers)
start = time.time()
sorted_numbers = b.sort(numbers)
end = time.time()
time_taken = end-start
print("Sorted list:", sorted_numbers)
print("Time taken:",time_taken)