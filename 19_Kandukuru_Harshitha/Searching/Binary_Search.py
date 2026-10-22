def binary_search(arr,target):
    left=0
    right=len(arr)-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return -1

arr=[2,4,6,8,10,12]
key=int(input("Enter the element to be searched:"))
result=binary_search(arr,key)
if key ==-1:
    print("Element Not Found")
else:
    print("Element Found at position:",result+1)

        