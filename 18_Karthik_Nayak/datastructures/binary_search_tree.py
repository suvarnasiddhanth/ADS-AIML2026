class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._add_node(self.root, value)

    def _add_node(self, current, value):
        if current is None:
            return Node(value)

        if value < current.value:
            current.left = self._add_node(current.left, value)
        elif value > current.value:
            current.right = self._add_node(current.right, value)

        return current

    def search(self, current, target):
        if current is None or current.value == target:
            return current

        if target < current.value:
            return self.search(current.left, target)

        return self.search(current.right, target)

    def inorder(self, current):
        if current is not None:
            self.inorder(current.left)
            print(current.value, end=" ")
            self.inorder(current.right)


def main():
    tree = BinarySearchTree()

    while True:
        print("\n--- Binary Search Tree Menu ---")
        print("1. Insert a value")
        print("2. Search for a value")
        print("3. Display inorder traversal")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            try:
                number = int(input("Enter the value to insert: "))
                tree.insert(number)
                print("Value inserted (duplicate values are ignored).")
            except ValueError:
                print("Please enter a valid integer.")

        elif choice == "2":
            if tree.root is None:
                print("The tree is empty. Insert a value first.")
                continue

            try:
                target = int(input("Enter the value to search for: "))
                result = tree.search(tree.root, target)

                if result is not None:
                    print(f"{target} found in the BST.")
                else:
                    print(f"{target} not found in the BST.")
            except ValueError:
                print("Please enter a valid integer.")

        elif choice == "3":
            if tree.root is None:
                print("The tree is empty. Insert some values first.")
            else:
                print("Inorder traversal:")
                tree.inorder(tree.root)
                print()

        elif choice == "4":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Select an option from 1 to 4.")


if __name__ == "__main__":
    main()
