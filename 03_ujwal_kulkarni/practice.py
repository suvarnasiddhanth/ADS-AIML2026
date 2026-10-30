#singly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = None

def insertFront(data):
    global head 
    newNode = Node(data)

    newNode.next = head
    head = newNode

def insertEnd(data):
    global head
    newNode = Node(data)

    if head is None:
        head = newNode
        return
    
    curr = head
    while curr.next is not None:
        curr = curr.next

    curr.next = newNode

def deleteNode(data):
    global head

    if head is None:
        print("list is empty")
        return
    
    if head.data == data:
        head = head.next
        return 
    
    curr = head
    while curr.next is not None and curr.next.data != data:
        curr = curr.next

    if curr.next is None:
        print("Element not found")
    else:
        curr.next = curr.next.next

def display():
    curr = head

    if curr is None:
        print("List is empty")
        return
    
    while curr is not None:
        print(curr.data, end=" -> ")
        curr = curr.next

    print("None")

while True:
    print("\n1. Insert at the beginning ")
    print("2. Insert at the end")
    print("3. Delete by value")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter choice:"))

    if choice == 1:
        data = int(input("enter a value:"))
        insertFront(data)

    elif choice == 2:
        data = int(input("Enter a value:"))
        insertEnd(data)

    elif choice == 3:
        data = int(input("ENter the value:"))
        deleteNode(data)

    elif choice == 4:
        display()

    elif choice == 5:
        break

    else:
        print("Invalide choice!")


#doubly linked list
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

head = None

def insertFront(data):
    global head
    newNode = Node(data)

    if head is None:
        head = newNode
    else:
        newNode.next = head
        head.prev = newNode
        head = newNode

def insertEnd(data):
    global head
    newNode = Node(data)

    if head is None:
        head = newNode
        return
    
    curr = head
    while curr.next is not None:
        curr = curr.next

    curr.next = newNode
    newNode.prev = curr

def deleteFront():
    global head 

    if head is None:
        print("list is empty")
        return
    
    head = head.next 

    if head is not None:
        head.prev = None

def deleteEnd():
    global head 

    if head is None:
        print("list is empty")
        return 
    
    if head.next is None:
        head = None
        return
    
    curr = head

    while curr.next is not None:
        curr = curr.next
    
    curr.prev.next = None

def display():
    curr = head

    if curr is None:
        print("List is empty")
        return
    
    while curr is not None:
        print(curr.data, end =" <-> ")
        curr = curr.next

    print("None")

while True:
    print("\n1. insert at the front")
    print("2. insert at the end")
    print("3. delete at the front")
    print("4. delete at the end")
    print("5. display")
    print("6. exit")

    choice = int(input("Enter the choice:"))

    if choice == 1:
        data = int(input("Enter value:"))
        insertFront(data)

    elif choice == 2:
        data = int(input("enter value:"))
        insertEnd(data)

    elif choice == 3:
        deleteFront()

    elif choice == 4:
        deleteEnd()

    elif choice == 5:
        display()

    elif choice == 6:
         break

    else:
         print("Invalide choice!")

#queue using linked list
class Node:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description
        self.next = None

front = None
rear = None

def insert(id, name, description):
    global front, rear

    newNode = Node(id, name, description)

    if front is None:
        front = rear = newNode
    else:
        rear.next = newNode
        rear = newNode

def display():
    curr = front

    if front is None:
        print("no pending issue, queue is empty")
        return
    
    while curr is not None:
        print("ID:", curr.id)
        print("Name:", curr.name)
        print("Issue:",curr.description)
        print()
        curr = curr.next 

def deletefront():
    global front, rear

    if front is None:
        print("no pending issues, queue is empty")
        return
    
    print("processed issue:", front.id, front.name)

    front = front.next

    if front is None:
        rear = None

    display()

def search(id):
    curr = front

    while curr is not None:
        if curr.id == id:
            print("ID:", curr.id)
            print("Name:", curr.name)
            print("Issue:", curr.description)
            return
        curr = curr.next 

    print("Issue not found")

def deletebyid(id):
    global front, rear

    curr = front
    prev = None

    while curr is not None and curr.id != id:
        prev = curr
        curr = curr.next

    if curr is None:
        print("Issue not found")
        return 
    
    if prev is None:
        front = curr.next 
    else:
        prev.next = curr.next 

    if curr == rear:
        rear = prev

    print("Issue deleted:", id)

insert(101, "ASha", "lab computer issue")
insert(102, "Ravi", "wifi issue")
search(102)
deletebyid(101)
display()
deletefront()


#queue->singly
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

front = None
rear = None

def enqueue(data):
    global front, rear

    newNode = Node(data)

    if front is None:
        front = rear = newNode
    else:
        rear.next = newNode
        rear = newNode

def dequeue():
    global front, rear

    if front is None:
        print("QUeue is empty")
        return 
    
    print("Deleted:", front.data)
    front = front.next

    if front is None:
        rear = None

def display():
    curr = front

    if front is None:
        print("queue is empty")
        return
    
    while curr is not None:
        print(curr.data, end =" -> ")
        curr = curr.next
    print("None")

enqueue(10)
enqueue(20)
enqueue(30)
display()

dequeue()
display()

#queue->DLL
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


front = None
rear = None


def enqueue(data):
    global front, rear

    newNode = Node(data)

    if front is None:
        front = rear = newNode
    else:
        rear.next = newNode
        newNode.prev = rear
        rear = newNode


def dequeue():
    global front, rear

    if front is None:
        print("Queue is empty")
        return

    print("Deleted:", front.data)
    front = front.next

    if front is None:
        rear = None
    else:
        front.prev = None


def display():
    curr = front

    if front is None:
        print("Queue is empty")
        return

    while curr is not None:
        print(curr.data, end=" <-> ")
        curr = curr.next

    print("None")


enqueue(10)
enqueue(20)
enqueue(30)

display()
dequeue()
display()


#stack using LL
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

top = None

def push(data):
    global top

    newNode = Node(data)
    newNode.next = top
    top = newNode

def pop():
    global top

    if top is None:
        print("stack is empty")
        return 
    
    print("popped:", top.data)
    top = top.next

def peek():
    if top is None:
        print("stack is empty")
    else:
        print("top element:", top.data)

def display():
    curr = top

    if top is None:
        print("stack is empty")
        return
    
    while curr is not None:
        print(curr.data, end =" -> ")
        curr = curr.next
    print("None")

push(10)
push(20)
push(30)

display()
peek()
pop()
display()





#stack using an array
stack = []

def push(data):
    stack.append(data)

def pop():
    if len(stack) == 0:
        print("stack is empty")
        return
    
    print("popped:", stack.pop())

def peek():
    if len(stack) == 0:
        print("stack is empty")
    else:
        print("top element:",stack[-1])

def display():
    if len(stack) == 0:
        print("stack is empty")
        return
    print(stack[::-1])

push(10)
push(20)
push(30)
display()
peek()
pop()
display()




#linear search
def linsearch(arr, key):
    count = 0

    for i in range(len(arr)):
        count += 1

        if arr[i] == key:
            print("element found at index", i)
            print("comparisons:", count)
            return
        
    print("element not found")
    print("comparisons:", count)

arr = [10,25,30,45,50]
linsearch(arr, 45)





#binary search
def binsearch(arr, key):
    low = 0
    high = len(arr)-1
    count = 0

    while low <= high:
        mid = (low + high) // 2
        count += 1

        if arr[mid] == key:
            print("element found at index", mid)
            print("comparisons:", count)
            return
        
        elif arr[mid] < key:
            low = mid + 1

        else:
            high = mid - 1

    print("element not found")
    print("comaparisons:", count)

arr = [10, 20, 30, 40, 50, 60, 70]
binsearch(arr,60)





#bubble sort
def bubblesort(arr):
    n = len(arr)
    count = 0

    for i in range(n-1):
        for j in range(n - i - 1):
            count += 1

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    print("sorted array:", arr)
    print("comaprisons:", count)

arr = [3,5,8,6,0]
bubblesort(arr)
            


#selection sort 
def selectionsort(arr):
    n = len(arr)
    count = 0
     
    for i in range(n - 1):
        minIndex = i

        for j in range(i + 1, n):
            count += 1

            if arr[j] < arr[minIndex]:
                minIndex = j

        arr[i], arr[minIndex] = arr[minIndex], arr[i]
    
    print("Sorted array:", arr)
    print("Comparisons:", count)


arr = [5, 3, 8, 2]
selectionsort(arr)




#insertionsort
def insertionsort(arr):
    n = len(arr)

    for i in range(1,n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key: 
            arr[j + 1] = arr[j]
            j = j - 1

        arr[j+1] = key

    print("sorted array:",arr)
   
arr = [5,3,8,2,6,9]
insertionsort(arr)





# merge sort
def mergesort(arr):
    global count

    if len(arr) > 1:
        mid = len(arr) // 2

        left = arr[:mid]
        right = arr[mid:]

        mergesort(left)
        mergesort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            count += 1

            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1

            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    return arr


arr = [5, 3, 8, 2, 6, 9]
count = 0

print("Sorted array:", mergesort(arr))
print("Comparisons:", count)




#quick sort
count = 0

def partition (arr, low, high):
    global count

    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        count +=1

        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def quicksort (arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quicksort(arr, low, p - 1)
        quicksort(arr, p + 1, high)

arr = [5,3,8,2,6,1]
quicksort(arr, 0, len(arr)-1)

print("sorted array:", arr)
print("comparisons:", count)





#heapsort
count = 0

def heapify(arr, n, i):
    global count

    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n:
        count += 1
        if arr[left] > arr[largest]:
            largest = left

    if right < n:
        count += 1
        if arr[right] > arr[largest]:
            largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    # Build Max Heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Move largest element to the end
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

    print("Sorted array:", arr)
    print("Comparisons:", count)


arr = [4, 10, 3, 5, 1]
heap_sort(arr)





#binary tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


root = Node(10)
root.left = Node(5)
root.right = Node(20)

root.left.left = Node(3)
root.left.right = Node(7)

print("Root:", root.data)
print("Left child:", root.left.data)
print("Right child:", root.right.data)






#traversal
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")

root = Node(10)
root.left = Node(5)
root.right = Node(20)
root.left.left = Node(3)
root.left.right = Node(7)

print("Inorder:")
inorder(root)

print("\nPreorder:")
preorder(root)

print("\nPostorder:")
postorder(root)





#BST
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, data):
    if root is None:
        return Node(data)
    
    if data < root.data:
        root.left = insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.right, data)

    return root

def search(root, key):
    if root is None or root.data == key:
        return root

    if key < root.data:
        return search(root.left, key)
    else:
        return search(root.right, key)


def minValueNode(root):
    current = root

    while current.left:
        current = current.left

    return current


def delete(root, key):
    if root is None:
        return root

    if key < root.data:
        root.left = delete(root.left, key)

    elif key > root.data:
        root.right = delete(root.right, key)

    else:
        # Case 1: No left child
        if root.left is None:
            return root.right

        # Case 2: No right child
        elif root.right is None:
            return root.left

        # Case 3: Two children
        temp = minValueNode(root.right)
        root.data = temp.data
        root.right = delete(root.right, temp.data)

    return root


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


root = None

for value in [50, 30, 70, 20, 40]:
    root = insert(root, value)

print("Inorder traversal:")
inorder(root)

key = 40
if search(root, key):
    print("\nElement found")
else:
    print("\nElement not found")






#circularqueue
class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def enqueue(self, data):
        if (self.rear + 1) % self.size == self.front:
            print("Queue is full")
            return

        if self.front == -1:
            self.front = 0

        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = data

    def dequeue(self):
        if self.front == -1:
            print("Queue is empty")
            return

        print("Deleted:", self.queue[self.front])

        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

    def display(self):
        if self.front == -1:
            print("Queue is empty")
            return

        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print()


q = CircularQueue(5)
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()
q.dequeue()
q.enqueue(40)
q.display()





#circularLL
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insertEnd(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            newNode.next = self.head
            return

        curr = self.head

        while curr.next != self.head:
            curr = curr.next

        curr.next = newNode
        newNode.next = self.head

    def display(self):
        if self.head is None:
            print("List is empty")
            return

        curr = self.head

        while True:
            print(curr.data, end=" ")
            curr = curr.next

            if curr == self.head:
                break

        print()


cll = CircularLinkedList()
cll.insertEnd(10)
cll.insertEnd(20)
cll.insertEnd(30)
cll.display()
