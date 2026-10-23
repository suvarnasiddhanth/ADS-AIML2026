
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)

        if self.root is None:
            self.root = new_node
            return

        queue = [self.root]

        while queue:
            current = queue.pop(0)

            if current.left is None:
                current.left = new_node
                return
            else:
                queue.append(current.left)

            if current.right is None:
                current.right = new_node
                return
            else:
                queue.append(current.right)

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

    def count_nodes(self, root):
        if root is None:
            return 0

        return (1 + self.count_nodes(root.left)
                  + self.count_nodes(root.right))


def main():
    tree = BinaryTree()

    while True:
        print("\n1. Insert node")
        print("2. Inorder traversal")
        print("3. Preorder traversal")
        print("4. Postorder traversal")
        print("5. Count nodes")
        print("6. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            data = int(input("Enter data: "))
            tree.insert(data)

        elif choice == 2:
            print("Inorder:", end=" ")
            tree.inorder(tree.root)
            print()

        elif choice == 3:
            print("Preorder:", end=" ")
            tree.preorder(tree.root)
            print()

        elif choice == 4:
            print("Postorder:", end=" ")
            tree.postorder(tree.root)
            print()

        elif choice == 5:
            count = tree.count_nodes(tree.root)
            print("Total number of nodes:", count)

        elif choice == 6:
            print("Exiting program")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
