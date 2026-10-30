"""
Binary Tree (linked representation)

New values are inserted in LEVEL ORDER: each one goes into the first empty
spot, top to bottom, left to right. This keeps the tree complete.
(For a tree that keeps values in sorted order, see bst.py.)

Run on its own:     python tree.py
Or from main menu:  python main.py
"""

from collections import deque


class TreeNode:                 # in the exam you can just call this Node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Insert in level order (first empty spot)        Time O(n), Space O(w)
def insert(root, value):
    new_node = TreeNode(value)
    if root is None:
        return new_node
    q = deque([root])
    while q:
        node = q.popleft()
        if node.left is None:
            node.left = new_node
            return root
        q.append(node.left)
        if node.right is None:
            node.right = new_node
            return root
        q.append(node.right)
    return root


# Preorder  (Root, Left, Right)                    Time O(n), Space O(h)
def preorder(node):
    if node is not None:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right)


# Inorder  (Left, Root, Right)                     Time O(n), Space O(h)
def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.data, end=" ")
        inorder(node.right)


# Postorder  (Left, Right, Root)                   Time O(n), Space O(h)
def postorder(node):
    if node is not None:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=" ")


# Breadth-first / level order                      Time O(n), Space O(w)
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


# Search (any order: the tree is not sorted)       Time O(n)
def search(node, value):
    if node is None:
        return False
    if node.data == value:
        return True
    return search(node.left, value) or search(node.right, value)


# Height = edges on the longest root-to-leaf path (empty tree = -1)
def height(node):
    if node is None:
        return -1
    return 1 + max(height(node.left), height(node.right))


def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)


def count_leaves(node):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return 1
    return count_leaves(node.left) + count_leaves(node.right)


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


tree_root = None        # kept here, so the tree stays when you go back to the main menu


def menu():
    global tree_root
    while True:
        print("\n------ BINARY TREE ------")
        print("1. Insert a value")
        print("2. Insert several values")
        print("3. Preorder traversal")
        print("4. Inorder traversal")
        print("5. Postorder traversal")
        print("6. Level order (breadth-first) traversal")
        print("7. Search")
        print("8. Height, node count and leaf count")
        print("9. Display tree")
        print("0. Back")
        choice = read_int("Enter choice: ")

        if choice in (3, 4, 5, 6, 9) and tree_root is None:
            print("Tree is empty.")
        elif choice == 1:
            value = read_int("Enter value: ")
            tree_root = insert(tree_root, value)
            print(value, "inserted.")
        elif choice == 2:
            values = read_int_list("Enter values separated by spaces: ")
            for value in values:
                tree_root = insert(tree_root, value)
            print(len(values), "value(s) inserted.")
        elif choice == 3:
            print("Preorder:", end=" ")
            preorder(tree_root)
            print()
        elif choice == 4:
            print("Inorder:", end=" ")
            inorder(tree_root)
            print()
        elif choice == 5:
            print("Postorder:", end=" ")
            postorder(tree_root)
            print()
        elif choice == 6:
            print("Level order:", end=" ")
            breadth_first(tree_root)
            print()
        elif choice == 7:
            value = read_int("Enter value to search: ")
            if search(tree_root, value):
                print(value, "found in the tree.")
            else:
                print(value, "not found.")
        elif choice == 8:
            print("Height:", height(tree_root))
            print("Nodes :", count_nodes(tree_root))
            print("Leaves:", count_leaves(tree_root))
        elif choice == 9:
            print("(sideways: root on the left, right subtree on top)")
            display_tree(tree_root)
        elif choice == 0:
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    menu()
