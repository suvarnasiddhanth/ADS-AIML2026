def linear_search(a, key):
    for i, j in enumerate(a):
        if j==key:
            return i
    return -1

print(linear_search([3,5,4,6,77], 77))