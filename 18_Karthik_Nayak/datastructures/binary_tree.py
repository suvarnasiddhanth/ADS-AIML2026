class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
            return

        pending_nodes = [self.root]

        while pending_nodes:
            parent = pending_nodes.pop(0)

            if parent.left is None:
                parent.left = new_node
                return
            pending_nodes.append(parent.left)

            if parent.right is None:
                parent.right = new_node
                return
            pending_nodes.append(parent.right)

    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(node.value, end=" ")
            self.inorder(node.right)

    def preorder(self, node):
        if node is not None:
            print(node.value, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node is not None:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.value, end=" ")


def main():
    tree = BinaryTree()

    while True:
        print("\n--- Binary Tree Menu ---")
        print("1. Insert a value")
        print("2. Inorder traversal")
        print("3. Preorder traversal")
        print("4. Postorder traversal")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            try:
                value = int(input("Enter a number to insert: "))
                tree.insert(value)
                print("Value inserted.")
            except ValueError:
                print("Please enter a valid integer.")

        elif choice == "2":
            if tree.root is None:
                print("The tree is empty. Insert some values first.")
            else:
                print("Inorder:")
                tree.inorder(tree.root)
                print()

        elif choice == "3":
            if tree.root is None:
                print("The tree is empty. Insert some values first.")
            else:
                print("Preorder:")
                tree.preorder(tree.root)
                print()

        elif choice == "4":
            if tree.root is None:
                print("The tree is empty. Insert some values first.")
            else:
                print("Postorder:")
                tree.postorder(tree.root)
                print()

        elif choice == "5":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Select a number from 1 to 5.")


if __name__ == "__main__":
    main()
