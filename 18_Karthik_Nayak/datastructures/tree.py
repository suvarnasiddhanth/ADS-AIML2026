class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)


def find_node(root, value):
    if root is None:
        return None

    if root.data == value:
        return root

    for child in root.children:
        found = find_node(child, value)
        if found is not None:
            return found

    return None


def display(root, level=0):
    if root is None:
        return

    print("  " * level + str(root.data))
    for child in root.children:
        display(child, level + 1)


def main():
    root = None

    while True:
        print("\n--- General Tree Menu ---")
        print("1. Create root node")
        print("2. Add child node")
        print("3. Display tree")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            if root is not None:
                print("The root already exists. Start a new run to create another tree.")
                continue

            value = input("Enter root value: ").strip()
            if not value:
                print("Value cannot be empty.")
                continue

            root = Node(value)
            print("Root node created.")

        elif choice == "2":
            if root is None:
                print("Create the root node first.")
                continue

            parent_value = input("Enter the parent node value: ").strip()
            parent = find_node(root, parent_value)

            if parent is None:
                print("Parent node not found.")
                continue

            child_value = input("Enter the child node value: ").strip()
            if not child_value:
                print("Value cannot be empty.")
                continue

            parent.add_child(Node(child_value))
            print("Child node added.")

        elif choice == "3":
            if root is None:
                print("The tree is empty. Create the root node first.")
            else:
                print("\nTree structure:")
                display(root)

        elif choice == "4":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()