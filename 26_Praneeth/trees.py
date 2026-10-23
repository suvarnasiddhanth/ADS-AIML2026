tree=[23, 89, 45, 19, 60, 73]

def left_child(i):
    index=2*i+1
    if index<len(tree):
        return tree[index]
    return None

def right_child(i):
    index=2*i+2
    if index<len(tree):
        return tree[index]
    return None

def parent(i):
    index=(i-1)//2
    if i!=0:
        return tree[index]
    return None

def size():
    return len(tree)

def is_empty():
    return len(tree)==0

print(left_child(2))

print(right_child(1))

print("size of tree:", size())
print("empty:", is_empty())
