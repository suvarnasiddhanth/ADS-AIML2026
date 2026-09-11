class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, data):
    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.right, data)

    return root


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")


root = None

while True:
    print("\n\n--- Binary Search Tree Menu ---")
    print("1. Insert")
    print("2. Inorder Traversal")
    print("3. Preorder Traversal")
    print("4. Postorder Traversal")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter value to insert: "))
        root = insert(root, value)
        print("Value inserted.")

    elif choice == 2:
        print("Inorder:", end=" ")
        inorder(root)

    elif choice == 3:
        print("Preorder:", end=" ")
        preorder(root)

    elif choice == 4:
        print("Postorder:", end=" ")
        postorder(root)

    elif choice == 5:
        print("Program ended.")
        break

    else:
        print("Invalid choice!")
