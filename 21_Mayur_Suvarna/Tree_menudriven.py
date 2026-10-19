
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert_node(self, root, value):
        if root is None:
            return Node(value)

        if value < root.data:
            root.left = self.insert_node(root.left, value)
        elif value > root.data:
            root.right = self.insert_node(root.right, value)

        return root

    def insert(self):
        value = int(input("Enter value: "))
        self.root = self.insert_node(self.root, value)
        print(value, "inserted")

    def search_node(self, root, value):
        if root is None:
            return False

        if root.data == value:
            return True
        elif value < root.data:
            return self.search_node(root.left, value)
        else:
            return self.search_node(root.right, value)

    def search(self):
        value = int(input("Enter value to search: "))
        if self.search_node(self.root, value):
            print("Value found")
        else:
            print("Value not found")

    def inorder(self, root):
        if root is not None:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    def preorder(self, root):
        if root is not None:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root is not None:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")

    def delete_node(self, root, value):
        if root is None:
            return None

        if value < root.data:
            root.left = self.delete_node(root.left, value)
        elif value > root.data:
            root.right = self.delete_node(root.right, value)
        else:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left

            temp = root.right
            while temp.left is not None:
                temp = temp.left

            root.data = temp.data
            root.right = self.delete_node(root.right, temp.data)

        return root

    def delete(self):
        value = int(input("Enter value to delete: "))

        if not self.search_node(self.root, value):
            print("Value not found")
        else:
            self.root = self.delete_node(self.root, value)
            print(value, "deleted")


tree = BST()

while True:
    print("\n--- Binary Search Tree Menu ---")
    print("1. Insert")
    print("2. Delete")
    print("3. Search")
    print("4. Inorder")
    print("5. Preorder")
    print("6. Postorder")
    print("7. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        tree.insert()
    elif choice == 2:
        tree.delete()
    elif choice == 3:
        tree.search()
    elif choice == 4:
        tree.inorder(tree.root)
        print()
    elif choice == 5:
        tree.preorder(tree.root)
        print()
    elif choice == 6:
        tree.postorder(tree.root)
        print()
    elif choice == 7:
        print("Exiting...")
        break
    else:
        print("Invalid choice")
