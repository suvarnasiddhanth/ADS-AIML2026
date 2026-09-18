class Node:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None
        
        
root= Node(10)

root.left = Node(5)
root.right = Node(15)
root.left.left = Node(3)
root.left.right = Node(7)
root.right.left = Node(12)

#inorder traversal Left-Root-Right
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data,end = " ")
        inorder(root.right)
        
#preorder traversal Root-Left-Right
def preorder(root):
    if root is not None:
        print(root.data,end = " ")
        preorder(root.left)
        preorder(root.right)
        
#postorder traversal Left-Right-Root
def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.data,end = " ")
        
        
print('Inorder: ')
inorder(root)

print('\nPreorder:')
preorder(root)

print('\nPostorder:')
postorder(root)