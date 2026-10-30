
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


def search(root, key):
    if root is None or key == root.data:
        return root

    if key < root.data:
        return search(root.left, key)
    else:
        return search(root.right, key)


def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


def preorder(root):
    if root is not None:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")


def min_val(root):
    current = root

    while current.left is not None:
        current = current.left

    return current


def delete(root, key):
    if root is None:
        return None

    if key < root.data:
        root.left = delete(root.left, key)

    elif key > root.data:
        root.right = delete(root.right, key)

    else:
        if root.left is None and root.right is None:
            return None

        elif root.left is None:
            return root.right

        elif root.right is None:
            return root.left

        else:
            successor = min_val(root.right)
            root.data = successor.data
            root.right = delete(root.right, successor.data)

    return root


# Menu-driven program

root = None

while True:
    print("\n\n----- BINARY SEARCH TREE MENU -----")
    print("1. Insert")
    print("2. Search")
    print("3. Inorder Traversal")
    print("4. Preorder Traversal")
    print("5. Postorder Traversal")
    print("6. Delete")
    print("7. Find Minimum Value")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        data = int(input("Enter value to insert: "))
        root = insert(root, data)
        print("Element inserted successfully.")

    elif choice == '2':
        key = int(input("Enter value to search: "))
        result = search(root, key)

        if result is not None:
            print("Element found:", key)
        else:
            print("Element not found:", key)

    elif choice == '3':
        print("Inorder Traversal: ", end="")
        if root is None:
            print("Tree is empty!")
        else:
            inorder(root)
            print()

    elif choice == '4':
        print("Preorder Traversal: ", end="")
        if root is None:
            print("Tree is empty!")
        else:
            preorder(root)
            print()

    elif choice == '5':
        print("Postorder Traversal: ", end="")
        if root is None:
            print("Tree is empty!")
        else:
            postorder(root)
            print()

    elif choice == '6':
        key = int(input("Enter value to delete: "))

        if search(root, key) is None:
            print("Element not found!")
        else:
            root = delete(root, key)
            print("Element deleted successfully.")

    elif choice == '7':
        if root is None:
            print("Tree is empty!")
        else:
            print("Minimum value:", min_val(root).data)

    elif choice == '8':
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")
