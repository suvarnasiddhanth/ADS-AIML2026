def bubble_sort(a):
    n=len(a)
    for i in range(n-1):
        swapped=False
        for j in range(n-1-i):
            if a[j]>a[j+1]:
                a[j], a[j+1]=a[j+1], a[j]
                swapped=True
        if swapped==False:
            break
    return a

print(bubble_sort([2, 1, 90, 56, 2, 3, 4, 4]))