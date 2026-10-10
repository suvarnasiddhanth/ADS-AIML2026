class QuickSort:
    def __init__(self, arr):
        self.arr = arr

    def quick_sort(self, low, high):
        if low < high:
            pivot_index = self.partition(low, high)

            self.quick_sort(low, pivot_index - 1)
            self.quick_sort(pivot_index + 1, high)

        return self.arr

    def partition(self, low, high):
        pivot = self.arr[high]
        i = low - 1

        for j in range(low, high):
            if self.arr[j] <= pivot:
                i += 1
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

        self.arr[i + 1], self.arr[high] = self.arr[high], self.arr[i + 1]

        return i + 1


arr = [4, 9, 10, 0, 6, 8]

obj = QuickSort(arr)
obj.quick_sort(0, len(arr) - 1)

print("The sorted array is:", obj.arr)
