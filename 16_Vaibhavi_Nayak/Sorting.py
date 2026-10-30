def BubbleSort(list):
    length=len(list)
    for i in range(1,length):
        swapped=False
        for j in range(0,length-i):
            if list[j]>list[j+1]:
                swapped=True
                list[j],list[j+1]=list[j+1],list[j]
        if swapped==False:
                return list
    return list

l1=[5,2,7,4,3]
result=BubbleSort(l1)
print(result)

def SelectionSort(list):
    length=len(list)
    for i in range(0,length-1):
        smallest=i
        for j in range(i+1,length):
            if list[smallest]>list[j]:
                smallest=j

        list[i],list[smallest]=list[smallest],list[i]
    return list

l2=[5,2,7,4,3]
result2=SelectionSort(l2)
print(result2)

def MergeSort(list):
    if len(list)<=1:
        return list
    mid=len(list)//2
    left=MergeSort(list[:mid])
    right = MergeSort(list[mid:])
    return Merge(left,right)



def Merge(left,right):
    i=0
    j=0
    result=[]
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1

    result.extend(left[i:])
    result.extend(right[j:])

    return result



l3=[5,2,7,4,3]
result3=MergeSort(l3)
print(result3)

def InsertionSort(arr):
    length=len(arr)
    for i in range(1,length):
        j=i-1
        key=arr[i]
        while j>=0 and arr[j]>key:
            arr[j+1],arr[j]=arr[j],arr[j+1]
            j-=1
        arr[j+1]=key
    return arr

l4=[5,2,7,4,3]
result4=InsertionSort(l4)
print(result4)

def QuickSort(arr,low,high):
    if low<high:
        pivot = Partition(arr,low,high)
        QuickSort(arr,low,pivot-1)
        QuickSort(arr,pivot+1,high)

    return arr

def Partition(arr,low,high):
    pivot=high
    i=low-1
    for j in range(low,high):
        if arr[j] <= arr[pivot]:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[pivot] = arr[pivot],arr[i+1]
    return i+1

l5=[5,2,7,4,3]
result5=QuickSort(l5,0,len(l5)-1)
print(result5)

def Heapify(arr,n,i):
    largest = i
    left=2*i+1
    right=2*i+2

    if left<n and arr[left]>arr[largest]:
        largest=left
    if right<n and arr[right]>arr[largest]:
        largest=right
    if largest!=i:
        arr[largest],arr[i]=arr[i],arr[largest]
        Heapify(arr,n,largest)

def HeapSort(arr):
    n=len(arr)

    for i in range(n//2-1,-1,-1):
        Heapify(arr,n,i)

    for i in range(n-1,0,-1):
        arr[i],arr[0]=arr[0],arr[i]
        Heapify(arr,i,0)

    return arr

arr = [5, 2, 7, 4, 3]
print(HeapSort(arr))

