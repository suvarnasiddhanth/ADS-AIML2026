class Bubble_Sort:
    def __init__(self, arr):
        self.arr=arr
    def sort(self):
        n=len(self.arr)
        for i in range(n):
            for j in range(0,n-i-1):
                if self.arr[j]>self.arr[j+1]:
                    self.arr[j],self.arr[j+1]=self.arr[j+1],self.arr[j]
        return self.arr

arr=[64,34,25,12,22,11,90]
bubble_sort=Bubble_Sort(arr)
sorted_arr=bubble_sort.sort()
print("Sorted Array:", sorted_arr)