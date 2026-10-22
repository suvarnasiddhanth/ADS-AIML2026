def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1
arr=[2,4,6,8,10,12]
key=int(input("Enter the element to be searched:"))
result=linear_search(arr,key)
if result==-1:
    print("Element Not Found")
else:
    print("Element Found at position:",result+1)
    