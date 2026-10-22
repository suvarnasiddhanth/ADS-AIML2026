class InsertionSort:
    def __init__(self, arr):
        self.arr = arr
    def insertion_sort(self):
        for i in range(1,len(self.arr)):
            key=self.arr[i]
            j=i-1
            while j>=0 and key< self.arr[j]:
                self.arr[j+1]=self.arr[j]
                j=j-1
            self.arr[j+1]=key
        return self.arr


arr=[12,11,13,5,6]
sort=InsertionSort(arr)
sorted_arr=sort.insertion_sort()
print("Sorted Array:",sorted_arr)