class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def create_tree():
    data = int(input("Enter root value (0 to cancel): "))

    if data == 0:
        return None

    root = Node(data)
    queue = [root]

    while queue:
        current = queue.pop(0)

        # Left child
        data = int(input(f"Enter left child of {current.data} (0 for none, -1 to finish): "))

        if data == -1:
            break

        if data != 0:
            current.left = Node(data)
            queue.append(current.left)

        # Right child
        data = int(input(f"Enter right child of {current.data} (0 for none, -1 to finish): "))

        if data == -1:
            break

        if data != 0:
            current.right = Node(data)
            queue.append(current.right)

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
    print("\n----- BINARY TREE MENU -----")
    print("1. Create Tree")
    print("2. Inorder")
    print("3. Preorder")
    print("4. Postorder")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        root = create_tree()

        if root:
            print("Tree created successfully.")
        else:
            print("Tree creation cancelled.")

    elif choice == 2:
        if root is None:
            print("Tree is empty.")
        else:
            print("Inorder:", end=" ")
            inorder(root)
            print()

    elif choice == 3:
        if root is None:
            print("Tree is empty.")
        else:
            print("Preorder:", end=" ")
            preorder(root)
            print()

    elif choice == 4:
        if root is None:
            print("Tree is empty.")
        else:
            print("Postorder:", end=" ")
            postorder(root)
            print()

    elif choice == 5:
        print("Program ended.")
        break

    else:
        print("Invalid choice!")
