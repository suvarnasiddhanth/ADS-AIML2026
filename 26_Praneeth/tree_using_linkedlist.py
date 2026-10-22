from collections import deque

class Node:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None

root=Node(10)
root.left=Node(20)
root.right=Node(30)
root.left.left=Node(25)
root.left.right=Node(28)

root.right.left=Node(31)
root.right.right=Node(32)


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


def bfs(root):
    if root is None:
        return 

    q=deque([root])
    while q:
        n=q.popleft()
        print(n.data, end=" ")

        if n.left:
            q.append(n.left)

        if n.right:
            q.append(n.right)




print(inorder(root))
print(preorder(root))
print(postorder(root))

print(bfs(root))