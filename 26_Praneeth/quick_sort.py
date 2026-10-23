"""without partition"""
def quick_sort(a):
    if len(a)<=1:
        return a

    p=a[len(a)//2]
    return (quick_sort([x for x in a if x<p])+ [x for x in a if x == p]
            + quick_sort([x for x in a if x > p]))

print(quick_sort([2,3,47, 4,53,99]))

