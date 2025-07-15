# this is gonna be nice

# what we need in the tree i
# current task is to  have the populate fromt the list
from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def populate(self):
        value = int(input("Enter the value for the root node:"))
        self.root = Node(value)
        self._populate(self.root)


    def _populate(self, node):
        left = input(f"Do you want to insert on left {node.value}? Y/N: ")

        if left.lower() == "y":
            print("\nNOW YOU ENTERING VALUES :")
            while True:
                try:
                    value = int(input(f"Enter the value for the left node of the {node.value} >> "))
                    break
                except ValueError as e:
                    print(f"Error: {e}")

            node.left = Node(value)
            self._populate(node.left)
        else:
            print("No Left Child Added ")


        right = input(f"Do you want to insert on the right {node.value}? Y/N: ")
        if right.lower() == "y":
              print("\nNOW YOU ENTERING VALUES :")
              while True:
                  try:
                      value = int(input(f"Enter the value for the right node of the {node.value} >> "))
                      break
                  except ValueError as e:
                      print(f"Error: {e}")

              node.right = Node(value)
              self._populate(node.right)
        else:
              print("No Right Child Added ")


    def populate_from_list(self,list):
        self.root = Node(list[0])
        self._populate_from_list(self.root, list, 0)

    # currently using the level-order style list
    def _populate_from_list(self, node, list, index):
        # i --> parent
        # 2(i)+1 --> left child
        # 2*i+2 --> right child

        if index == len(list)+1:
            return

        if ((2*index)+1)<len(list) and list[(2*index)+1] is not None:
            node.left = Node(list[(2*index)+1])
        else:
            node.left = None

        if ((2*index)+2)<len(list) and list[(2*index)+2] is not None:
            node.right = Node(list[(2*index)+2])
        else:
            node.right = None

        if node.left:
            self._populate_from_list(node.left, list, (2*index)+1)
        if node.right:
            self._populate_from_list(node.right, list, (2*index)+2)


def populate_from_list_iterative(self, list):
    if not list or list[0] is None:
      self.root= None
      return
    self._populate_from_list_iterative(self, list)

def _populate_from_list_iterative(self, arr):
    self.root = Node(arr[0])
    queue = deque()
    queue.append((self.root, 0))

    while queue:
        node, i  = queue.popleft()

        left_index = (2*i)+1
        right_index = (2*i)+2

        if left_index<len(arr) and arr[left_index] is not None:
            node.left = Node(arr[left_index])
            queue.append((node.left, left_index))

        if right_index<len(arr) and arr[right_index] is not None:
            node.right = Node(arr[right_index])
            queue.append((node.right, right_index))


    def display(self):
        self._display()

    def _display(self):
        if self.root is None:
            return

        queue = deque([self.root])
        while queue:
            level_size = len(queue)

            for _ in range(level_size):
                curr_node = queue.popleft()
                print(curr_node.value, end = ' ')
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
            print()


    def display1(self):
        self._display1(self.root)

    def _display1(self, node, indent=""):
        if node is None:
            return

        print(indent+str(node.value))
        self._display1(node.left, indent+'\t')
        self._display1(node.right, indent+'\t')




if __name__ == "__main__":
    BT = BinaryTree()
    BT.populate()
    BT.display1()
