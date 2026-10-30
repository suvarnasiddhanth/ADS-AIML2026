class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST():
    def __init__(self):
        self.root = None

    def insert(self, root, data):
        if root is None:
            return Node(data)

        if data < root.data:
            root.left = self.insert(root.left, data)
        elif data > root.data:
            root.right = self.insert(root.right, data)
        return root

    def search(self, root, key):
        if root is None or root.data == key:
            return root
        if key < root.data:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end = " ")
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")

    def level_order(self, root):
        if root is None:
            print("Tree is empty")
            return

        queue = [root]

        while queue:
            current = queue.pop(0)
            print(current.data, end=" ")

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

    def find_min(self,root):
        if root is None:
            return None
        while root.left:
            root = root.left
        return root.data

    def find_max(self, root):
        if root is None:
            return None
        while root.right:
            root = root.right
        return root.data

    def delete(self, root, key):
        if root is None:
            return None
        if key<root.data:
            root.left = self.delete(root.left, key)
        elif key> root.data:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:  # CASE 1: Node has no left child
                return root.right
            if root.right is None: # CASE 2: Node has no right child
                return root.left

            successor = root.right  # CASE 3: Node has two children
            while successor.left:
                successor = successor.left
            root.data = successor.data
            root.right = self.delete(root.right, successor.data)
        return root

    def height(self, root):
        if root is None:
            return 0
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        return 1 + max(left_height, right_height)

    def count_nodes(self, root):
        if root is None:
            return 0
        return (1 + self.count_nodes(root.left) + self.count_nodes(root.right))

    def count_leaf_nodes(self, root):
        if root is None: 
            return 0
        if root.left is None and root.right is None:
            return 1
        return (self.count_leaf_nodes(root.left) + self.count_leaf_nodes(root.right))

def trees_menu():

    tree = BST()

    while True:
        print("\n--- BINARY SEARCH TREE ---")
        print("1. Insert")
        print("2. Search")
        print("3. Inorder Traversal")
        print("4. Preorder Traversal")
        print("5. Postorder Traversal")
        print("6. Level-order Traversal")
        print("7. Find Minimum")
        print("8. Find Maximum")
        print("9. Delete")
        print("10. Height of Tree")
        print("11. Count All Nodes")
        print("12. Count Leaf Nodes")
        print("13. Exit")

        choice = input("\nEnter the choice: ")

        if choice == "1":
            data = int(input("\nEnter the value: "))
            tree.root = tree.insert(tree.root, data)
            print("Node inserted")

        elif choice == "2":
            key = int(input("\nenter the key to search:"))
            result = tree.search(tree.root, key)
            if result: 
                print("element found")
            else: 
                print("element not found")

        elif choice == "3":
            print("\nInorder Traversal: ", end=" ")
            tree.inorder(tree.root)
            print()

        elif choice == "4":
            print("\nPreorder Traversal: ", end=" ")
            tree.preorder(tree.root)
            print()

        elif choice == "5":
            print("\nPostorder Traversal: ", end=" ")
            tree.postorder(tree.root)
            print()

        elif choice == "6":
            print("\nLevel order Traversal: ", end=" ")
            tree.level_order(tree.root)
            print()

        elif choice == "7":
            # Display the smallest value
            print("Minimum:", tree.find_min(tree.root))

        elif choice == "8":
            # Display the largest value
            print("Maximum:", tree.find_max(tree.root))

        elif choice == "9":
            # Delete the given value and update the root
            key = int(input("Enter value to delete: "))
            tree.root = tree.delete(tree.root, key)
            print("Deletion completed")

        elif choice == "10":
            # Display the height in nodes/levels
            print("Height of tree:", tree.height(tree.root))

        elif choice == "11":
            # Display the total number of nodes
            print("Total nodes:", tree.count_nodes(tree.root))

        elif choice == "12":
            # Display the number of leaf nodes
            print("Leaf nodes:", tree.count_leaf_nodes(tree.root))

        elif choice == "13":
            # Stop the menu loop
            print("Exiting program")
            break

        else:
            # Handle an invalid menu selection
            print("Invalid choice")

if __name__ == "__main__":
    trees_menu()