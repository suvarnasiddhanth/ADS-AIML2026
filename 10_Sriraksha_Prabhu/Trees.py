class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)


def display(root):
    if root is None:
        return

    print(root.data)

    for child in root.children:
        display(child)


def main():
    root = Node(1)

    child1 = Node(2)
    child2 = Node(3)
    child3 = Node(4)

    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(child3)
    display(root)


if __name__ == "__main__":
    main()
