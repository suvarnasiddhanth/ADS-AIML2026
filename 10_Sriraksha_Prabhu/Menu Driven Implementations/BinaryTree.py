
from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self):
        value = int(input("Enter value: "))
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
            print(value, "inserted")
            return

        q = deque([self.root])

        while q:
            temp = q.popleft()

            if temp.left is None:
                temp.left = new_node
                break
            else:
                q.append(temp.left)

            if temp.right is None:
                temp.right = new_node
                break
            else:
                q.append(temp.right)

        print(value, "inserted")

    def search(self):
        value = int(input("Enter value to search: "))
        q = deque()

        if self.root is not None:
            q.append(self.root)

        while q:
            temp = q.popleft()

            if temp.data == value:
                print("Value found")
                return

            if temp.left:
                q.append(temp.left)

            if temp.right:
                q.append(temp.right)

        print("Value not found")

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
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


tree = BinaryTree()

while True:
    print("\n--- Binary Tree Menu ---")
    print("1. Insert")
    print("2. Search")
    print("3. Inorder")
    print("4. Preorder")
    print("5. Postorder")
    print("6. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        tree.insert()
    elif choice == 2:
        tree.search()
    elif choice == 3:
        tree.inorder(tree.root)
        print()
    elif choice == 4:
        tree.preorder(tree.root)
        print()
    elif choice == 5:
        tree.postorder(tree.root)
        print()
    elif choice == 6:
        break
    else:
        print("Invalid choice")
