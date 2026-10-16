class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert(self.root, data)

    def _insert(self, root, data):
        if root is None:
            return Node(data)

        if data < root.data:
            root.left = self._insert(root.left, data)
        elif data > root.data:
            root.right = self._insert(root.right, data)

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
            print(root.data, end=" ")
            self.inorder(root.right)


def main():
    bst = BST()

    for value in [50, 30, 70, 20, 40, 60, 80]:
        bst.insert(value)

    print("Inorder traversal:")
    bst.inorder(bst.root)

    key = 40
    result = bst.search(bst.root, key)

    if result:
        print(f"\n{key} found in BST")
    else:
        print(f"\n{key} not found in BST")


if __name__ == "__main__":
    main()