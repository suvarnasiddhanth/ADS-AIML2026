class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class BinarySearchTree:
    def __init__(self):
        self.root=None
    def insert(self,data):
        new_node=Node(data)
        if self.root is None:
            self.root=new_node
            return
        current=self.root
        while True:
            if data<current.data:
                if current.left is None:
                    current.left=new_node
                    return
                current=current.left
            else:
                if current.right is None:
                    current.right=new_node
                    return
                current=current.right
    def inorder(self,root):
        if root is not None:
            self.inorder(root.left)
            print(root.data,end="")
            self.inorder(root.right)
    def preorder(self,root):
        if root is not None:
            print(root.data,end="")
            self.preorder(root.left)
            self.preorder(root.right)
    def postorder(self,root):
        if root is not None:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data,end="")
    def count_nodes(self,root):
        if root is None:
            return 0
        return (1+self.count_nodes(root.left)+self.count_nodes(root.right))
def main():
    bst=BinarySearchTree()
    while True:
        print("\nBinary Search Tree Operations Menu:")
        print("1. Insert")
        print("2. Inorder Traversal")
        print("3. Preorder Traversal")
        print("4. Postorder Traversal")
        print("5. Count Nodes")
        print("6. Exit")
        choice=int(input("Enter your choice (1-6):"))
        if choice==1:
            data=int(input("Enter the element to insert:"))
            bst.insert(data)
        elif choice==2:
            print("Inorder Traversal:",end=" ")
            bst.inorder(bst.root)
            print()
        elif choice==3:
            print("Preorder Traversal:",end=" ")
            bst.preorder(bst.root)
            print()
        elif choice==4:
            print("Postorder Traversal:",end=" ")
            bst.postorder(bst.root)
            print()
        elif choice==5:
            count=bst.count_nodes(bst.root)
            print("Total number of nodes in the BST:",count)
        elif choice==6:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")  

if __name__=="__main__":
    main()