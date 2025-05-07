# binary


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert(value, self.root)

    def _insert(self, value, node):
        if node is None:
            return Node(value)

        if value < node.value:
            node.left = self._insert(value, node.left)

        if value > node.value:
            node.right = self._insert(value, node.right)

        node.height = 1 + max(self.height(node.left), self.height(node.right))

        return node

    def populate(self, nums):
        for i in range(len(nums)):
            self.insert(nums[i])

    def populateSorted(self, nums):
        self._populateSorted(self, nums, 0, len(nums))

    def _populateSorted(self, nums, start, end):
        if start >= end:
            return

        mid = (start + end) // 2
        self.insert(nums[mid])

        self._populateSorted(nums, start, mid)
        self._populateSorted(nums, mid + 1, end)

    def balanced(self):
        return self._balanced(self.root)

    def height(self, node):
        if node is None:
            return 0
        return node.height

    def _balanced(self, node):
        if node is None:
            return True

        return (
            abs(self.height(node.left) - self.height(node.right)) <= 1
            and self._balanced(node.left)
            and self._balanced(node.right)
        )

    def display(self):
        self._display(self.root, "Root Node : ")

    def _display(self, node, details):
        if node is None:
            return

        print(details + str(node.value))
        self._display(node.left, f"Left  node of {node.value} : ")
        self._display(node.right, f"Right node of {node.value} : ")


if __name__ == "__main__":
    bst = BST()
    nums = list(map(int, input().split()))
    bst.populate(nums)
    bst.display()
    print("Balanced BST?", bst.balanced())
