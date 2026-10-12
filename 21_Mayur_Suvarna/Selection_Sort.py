def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[min_index],arr[i]=arr[i],arr[min_index]
        
    return arr

print(selection_sort([2,6,8,4,1,0,9]))