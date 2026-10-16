import time

class Lin_Search:
    def search(self,A,ele):
        n= len(A)
        for i in range(n):
            if A[i]==ele:
                return i
        return -1

b = Lin_Search()
numbers = [64, 34, 25, 12, 22, 11, 90]

ele = 22

start = time.time()
result = b.search(numbers,ele)
end = time.time()

if result==-1:
    print("Item not found")
else:
    print(f"Item found at {result+1}")

