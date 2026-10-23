def selection_sort(a):
    n=len(a)
    for i in range(n-1):
        m=i
        for j in range(i+1, n):
            if a[j]<a[m]:
                m=j
        a[m], a[i]=a[i], a[m]
    return a

print(selection_sort([1, 7, 2,34, 9,0]))