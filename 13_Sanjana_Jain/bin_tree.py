#to implement the binary tree and perform basic operations like insert delete update search
class Node:
    def __init__(self,data):
        self.value = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self,value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root,value)

    def _insert(self,node,value):
        if value < node.value:
            if node.left is None:
                node.left = value
            else:
                self._insert(node.left,value)

        elif value > node.value:
            if node.right is None:
                node.right = value
            else:
                self._insert(node.right,value) 


    def search(self,value):
        return self._search(self.root,value)

    def _search(self,node,value):
        if node is None:
            return False
        elif node.value == value:
            return True
        elif node.value< value:
            self._search(node.left,value)
        else:
            self._search(node.right,value)


    def inorder(self,node):
        if node:
            self.inorder(self,node.left)
            print(node.value,end=" ")
            self.inorder(self,node.right)

    def postorder(self,node):
        if node:
            self.preorder(self,node.left)
            self.preorder(self,node.right)
            print(node.value, end=" ")

    def preorder(self,node):
            if node:
                print(node.value, end=" ")
                self.preorder(self,node.left)
                self.preorder(self,node.right)
                
    def display(self):
        if self.head is None:
            print("list is empty")
            return
        current = self.head 
        while current is not None:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")
        print("\n")

tree = BinarySearchTree()

tree.insert(50)
tree.insert(30)
tree.insert(70)
tree.insert(20)
tree.insert(40)
tree.insert(60)
tree.insert(80)

print("Inorder:")
tree.inorder(tree.root)

print("\nPreorder:")
tree.preorder(tree.root)

print("\nPostorder:")
tree.postorder(tree.root)

print("\n\nSearch 40:", tree.search(40))
print("Search 90:", tree.search(90))




    
        
      
