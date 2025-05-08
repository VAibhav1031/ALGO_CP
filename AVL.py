class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


class AVL:
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

        node.height = 1 + max(self._height(node.left),
                              self._height(node.right))

        return self.rotate(node)

    def rotate(self, node):
        return self._rotate(node)

    def _rotate(self, node):
        # left Heavy
        # in this  leftchild - rightchild > 0 means we are left heavy
        # will see what is the  left - left and  left-right case
        # everything opposite will of the right heavy

        if (self._height(node.left) - self._height(node.right)) > 1:
            # left-left case
            # why we are doing this  .left .left , first build the normal left left tree and  then
            # calculate the thing like left.left tree height greater than  left.right  means we have left left case  ( ~/ vice versa for right-right case )
            if self._height(node.left.left) >= self._height(node.left.right):
                return self.rightRotate(node)

            # left-right case
            # for this  if  we have .left.left tree height less than .left.right will make  the situation of left-right
            if self._height(node.left.left) <= self._height(node.left.right):
                node.left = self.leftRotate(node.left)
                return self.rightRotate(node)

        # Right Heavy
        elif (self._height(node.left) - self._height(node.right)) < -1:
            # Right-Righ case
            if self._height(node.right.left) <= self._height(node.right.right):
                return self.leftRotate(node)

            # right-left case
            if self._height(node.right.left) >= self._height(node.right.right):
                node.right = self.rightRotate(node.right)
                return self.leftRotate(node)

        return node

    def rightRotate(self, p):
        c = p.left
        t2 = c.right

        c.right = p
        p.left = t2

        p.height = 1 + max(self._height(p.left), self._height(p.right))
        c.height = 1 + max(self._height(c.left), self._height(c.right))

        return c

    def leftRotate(self, c):
        p = c.right

        t2 = p.left

        p.left = c
        c.right = t2

        p.height = 1 + max(self._height(p.left), self._height(p.right))
        c.height = 1 + max(self._height(c.left), self._height(c.right))

        return p

    def populate(self, nums):
        for i in range(len(nums)):
            self.insert(nums[i])

    def populateSorted(self, nums):
        self._populateSorted(nums, 0, len(nums))

    def _populateSorted(self, nums, start, end):
        if start >= end:
            return

        mid = (start + end) // 2
        self.insert(nums[mid])

        self._populateSorted(nums, start, mid)
        self._populateSorted(nums, mid + 1, end)

    def balanced(self):
        return self._balanced(self.root)

    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if node is None:
            return -1
        return node.height

    def _balanced(self, node):
        if node is None:
            return True

        return (
            abs(self._height(node.left) - self._height(node.right)) <= 1
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
    avl = AVL()

    for i in range(1000):
        avl.insert(i)

    print(avl.height())
