class SelectionSort:
    def __init__(self,arr):
        self.arr=arr

    def selection_sort(self):
        n=len(self.arr)
        for i in range(n):
            min_index=i
            for j in range(i+1,n):
                if self.arr[j]<self.arr[min_index]:
                    min_index=j
            self.arr[i],self.arr[min_index]=self.arr[min_index],self.arr[i]
        return self.arr

arr=[64,25,12,22,11]
sort = SelectionSort(arr)
sorted_arr=sort.selection_sort()
print("Sorted Array:",sorted_arr)