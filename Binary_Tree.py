#  here we will gonna display basic  binary tree and display function


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def populate(self):
        value = int(input("Enter the root Node: "))
        self.root = Node(value)
        self._populate(self.root)

    def _populate(self, node):
        left = input(
            f"Do you want to enter left of Node - {node.value} ?  (y/n): \n")
        if left.lower() == "y":
            value = int(
                input(
                    f"Enter the value for the left of Node - {node.value} >> ")
            )
            node.left = Node(value)
            self._populate(node.left)

        right = input(
            f"Do you want to enter right of Node - {node.value} ? (y/n): \n")
        if right.lower() == "y":
            value = int(
                input(
                    f"Enter the value for the right of Node - {node.value} >> ")
            )
            node.right = Node(value)
            self._populate(node.right)

    def display(self):
        self._display(self.root)

    def _display(self, node, indent=""):
        if node is None:
            return

        print(indent + str(node.value))
        self._display(node.left, indent + "\t")
        self._display(node.right, indent + "\t")

    def prettyGoodDsiplay(self):
        self._prettyGoodDsiplay(self.root, 0)

    def _prettyGoodDisplay(self, node, level):
        if node is None:
            return

        self._prettyGoodDisplay(node.right, level + 1)

        if level != 0:
            for i in range(level - 1):
                print("|\t\t")

            print(f"-------->{node.value}")

        else:
            print(node.value)

        self._prettyGoodDisplay(node.left, level + 1)


# Usage
tree = BinaryTree()
tree.populate()
tree.display()
