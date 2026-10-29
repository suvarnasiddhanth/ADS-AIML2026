"""
Binary Search Tree (BST)

Rule at every node:  left subtree < node < right subtree.
Duplicate values are not inserted.

Run on its own:     python bst.py
Or from main menu:  python main.py
"""

from collections import deque


class TreeNode:                 # in the exam you can just call this Node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Search (iterative)                      Time O(h), Space O(1)
def search(root, target):
    current = root
    while current is not None:
        if target == current.data:
            return current
        elif target < current.data:
            current = current.left
        else:
            current = current.right
    return None


# Search (recursive)                      Time O(h), Space O(h)
def search_rec(root, target):
    if root is None:
        return None
    if target == root.data:
        return root
    if target < root.data:
        return search_rec(root.left, target)
    return search_rec(root.right, target)


# Insert                                  Time O(h), Space O(h)
def insert(root, value):
    if root is None:
        return TreeNode(value)
    if value < root.data:
        root.left = insert(root.left, value)
    elif value > root.data:
        root.right = insert(root.right, value)
    return root


# Smallest value: keep going left         Time O(h)
def find_min(node):
    current = node
    while current.left is not None:
        current = current.left
    return current


# Largest value: keep going right         Time O(h)
def find_max(node):
    current = node
    while current.right is not None:
        current = current.right
    return current


# Delete                                  Time O(h)
def delete(root, value):
    if root is None:
        return None
    if value < root.data:
        root.left = delete(root.left, value)
    elif value > root.data:
        root.right = delete(root.right, value)
    else:
        if root.left is None:           # leaf or only right child
            return root.right
        if root.right is None:          # only left child
            return root.left
        successor = find_min(root.right)    # two children: inorder successor
        root.data = successor.data
        root.right = delete(root.right, successor.data)
    return root


# Traversals                              Time O(n)
def inorder(node):              # gives SORTED order for a BST
    if node is not None:
        inorder(node.left)
        print(node.data, end=" ")
        inorder(node.right)


def preorder(node):
    if node is not None:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right)


def postorder(node):
    if node is not None:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=" ")


def breadth_first(root):
    if root is None:
        return
    q = deque([root])
    while q:
        node = q.popleft()
        print(node.data, end=" ")
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)


# Height = edges on the longest root-to-leaf path (empty tree = -1)
def height(node):
    if node is None:
        return -1
    return 1 + max(height(node.left), height(node.right))


# Print the tree sideways: root on the left, RIGHT subtree above, LEFT below
def display_tree(node, level=0):
    if node is not None:
        display_tree(node.right, level + 1)
        print("      " * level + str(node.data))
        display_tree(node.left, level + 1)


# ---------------------------------------------------------------------
# Menu
# ---------------------------------------------------------------------
def read_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def read_int_list(prompt):
    while True:
        try:
            return [int(x) for x in input(prompt).split()]
        except ValueError:
            print("Invalid input. Enter whole numbers separated by spaces.")


bst_root = None         # kept here, so the tree stays when you go back to the main menu


def menu():
    global bst_root
    while True:
        print("\n------ BINARY SEARCH TREE ------")
        print("1. Insert a value")
        print("2. Insert several values")
        print("3. Delete a value")
        print("4. Search")
        print("5. Inorder traversal (sorted)")
        print("6. Preorder traversal")
        print("7. Postorder traversal")
        print("8. Level order (breadth-first) traversal")
        print("9. Minimum and maximum")
        print("10. Height")
        print("11. Display tree")
        print("0. Back")
        choice = read_int("Enter choice: ")

        if choice in (5, 6, 7, 8, 9, 11) and bst_root is None:
            print("Tree is empty.")
        elif choice == 1:
            value = read_int("Enter value: ")
            if search(bst_root, value):
                print(value, "is already in the tree (duplicates are not allowed).")
            else:
                bst_root = insert(bst_root, value)
                print(value, "inserted.")
        elif choice == 2:
            values = read_int_list("Enter values separated by spaces: ")
            added = 0
            for value in values:
                if search(bst_root, value):
                    print("Skipped duplicate:", value)
                else:
                    bst_root = insert(bst_root, value)
                    added += 1
            print(added, "value(s) inserted.")
        elif choice == 3:
            value = read_int("Enter value to delete: ")
            if search(bst_root, value):
                bst_root = delete(bst_root, value)
                print(value, "deleted.")
            else:
                print(value, "not found in the tree.")
        elif choice == 4:
            value = read_int("Enter value to search: ")
            if search(bst_root, value):
                print(value, "found in the tree.")
            else:
                print(value, "not found.")
        elif choice == 5:
            print("Inorder:", end=" ")
            inorder(bst_root)
            print()
        elif choice == 6:
            print("Preorder:", end=" ")
            preorder(bst_root)
            print()
        elif choice == 7:
            print("Postorder:", end=" ")
            postorder(bst_root)
            print()
        elif choice == 8:
            print("Level order:", end=" ")
            breadth_first(bst_root)
            print()
        elif choice == 9:
            print("Minimum:", find_min(bst_root).data)
            print("Maximum:", find_max(bst_root).data)
        elif choice == 10:
            print("Height:", height(bst_root))
        elif choice == 11:
            print("(sideways: root on the left, right subtree on top)")
            display_tree(bst_root)
        elif choice == 0:
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    menu()
