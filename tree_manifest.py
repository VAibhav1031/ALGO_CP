# this is gonna be nice

# what we need in the tree i
# current task is to  have the populate fromt the list
from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 0

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
        self._populate_from_list_iterative(list)

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



    def inorder(self, node):
        # left Root right
        if node is None:
            return []


        left = self.inorder(node.left)
        right = self.inorder(node.right)

        return left+ [node.value] + right



    def postorder(self, node):
        #   left right root
        if node is None:
            return []


        left = self.postorder(node.left)
        right = self.postorder(node.right)

        return left+ right + [node.value]


    def preorder(self, node):
        #   left right root
        if node is None:
            return []


        left = self.preorder(node.left)
        right = self.preorder(node.right)

        return [node.value] + left + right


    def height(self, node, level):
        # okay height of the treee wile be  max(height of left-subtree,height of thr right-subtree)
        if node is None:
            return level

        left_subtree  = self.height(node.left, level + 1)
        right_subtree = self.height(node.right, level + 1)

        return max(left_subtree, right_subtree)

    def height1(self, node):
        if node is None:
            return 0
        return 1 + max(self.height1(node.left), self.height1(node.right))


    def tolist(self, node):
        #  we will use the level-order format
        if  node is None:
            return
        queue = deque([node])
        result = []
        while queue:
            curr_node = queue.popleft()
            if curr_node:
                result.append(curr_node.value)
                queue.append(curr_node.left)
                queue.append(curr_node.right)

            else:
                queue.append(None)

        return result


    def invert(self, node):
        if node is None:
            return

        node.left, node.right = node.right, node.left
        self.invert(node.left)
        self.invert(node.right)

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



class BST(BinaryTree):
    def __init__(self):
        super().__init__()
        self.root=None

    def height_bst(self, node):
        return self._height(node)

    def _height(self, node):
        if node is None:
            return -1
        return node.height

    def insert(self, value):
        self.root = self._insert(value, self.root)



    def _insert(self, value, node):
        if node is None:# it is  something  when we hit the base null value then we create a new node and return it  and it will save to desired location(left or right)
            new_node = Node(value)
            return new_node

        if value < node.value:
            node.left = self._insert(value, node.left)
        if value > node.value:
            node.right = self._insert(value, node.right)
        node.height = 1 + max(self.height_bst(node.left), self.height_bst(node.right))

        return self.self_balancing(node) #  if  everything goes right we are returning the node , at which changes were ocurred


    def populate(self, nums):
        for i in range(len(nums)):
            self.insert(nums[i])

    def _populate_sorted(self, nums):
        self.populated_sorted(nums, 0, len(nums))

    # preventing skewness if we got sorted array to populate
    def populated_sorted(self,nums, start, end):
        if start>=end:
            return

        mid = (start+end)//2
        self.insert(nums[mid])
        self.populated_sorted(nums,start, mid)
        self.populated_sorted(nums,mid+1, end)


    def isbalanced(self, node):
        return self._isbalanced(node)


    def _isbalanced(self, node):
        if node is None:
            return True

        return  abs(self.height_bst(node.left)-self.height_bst(node.right))<=1 and self._isbalanced(node.left) and self._isbalanced(node.right)

    def search(self, value):
        return self._search(value, self.root)

    def _search(self, val, node):
        if node is None:
            return False

        if node.value == val:
            return True

        elif val<node.value:
            return self._search(val, node.left)

        else:
            return self._search(val, node.right)


    def delete_value(self, value):
        return self.delete(value, self.root)

    def delete(self, val, node):#node is  acting as parent node/root node
        # delete then balance the tree(will do that later)
        if node is None:
            return None
        if val<node.value:
            node.left = self.delete(val, node.left)
        elif val>node.value:
            node.right = self.delete(val, node.right)
        else:
            if node.right is None and node.left is None:
                return None

            if node.left is None:
                return node.right

            if node.right is None:
                return node.left

            else:
                sucessor = self.get_min(node.right)
                node.value = sucessor.value
                node.right = self.delete(sucessor.value, node.right)


        return self.self_balancing(node)

    def get_min(self, node):
        while node.left:
            node = node.left
        return node

    def display_BST(self, node):
        self._display_BST(node,"The root of the Tree ")
    def _display_BST(self, node, details):
        if node is None:
            return

        print(details+ str(node.value))
        if node.left:
            self._display_BST(node.left,f"value of the left node  of {node.value} :")
        if node.right:
            self._display_BST(node.right,f"value of the right node  of {node.value} :")


    def self_balancing(self, node):
        if self._isbalanced(node):
            return node

        height_diff = self.height_bst(node.left) - self.height_bst(node.right)
        # you think how it will go
        if  height_diff > 1:
            # left heavy
            if (self.height_bst(node.left.left) - self.height_bst(node.left.right) > 0):
                # left-left heavy
                return self.right_rotate(node)
                # cause we have to  reassign the  tree node , if we dont it will destroy tree

            if (self.height_bst(node.left.left) - self.height_bst(node.left.right)<0):
               # left-right heavy
               node.left = self.left_rotate(node.left)
               return self.right_rotate(node)

        if height_diff<-1:
            # Right heavy
            if (self.height_bst(node.right.left) - self.height_bst(node.right.right) < 0):
                # right-right heavy
                return self.left_rotate(node)
                # cause we have to  reassign the  tree node , if we dont it will destroy tree

            if (self.height_bst(node.right.left) - self.height_bst(node.right.right)>0):
               # right-left heavy
               node.right = self.right_rotate(node.right)
               return self.left_rotate(node)


    def right_rotate(self, p):
        c = p.left
        t = c.right

        c.right = p
        p.left = t

        p.height = max(self.height_bst(p.left), self.height_bst(p.right)) + 1
        c.height = max(self.height_bst(c.left), self.height_bst(c.right)) + 1


        return c

    def left_rotate(self, c):
            p = c.right
            t = p.left

            p.left = c
            c.right = t

            p.height = max(self.height_bst(p.left), self.height_bst(p.right)) + 1
            c.height = max(self.height_bst(c.left), self.height_bst(c.right)) + 1

            return p

if __name__ == "__main__":
    BT = BinaryTree()
    BT.populate_from_list([1, 2, 3, 4, 5, 6, 7])
    bst = BST()
    bst.populated_sorted([1, 2, 3, 4, 5, 6, 7], 0, 7)
    bst.display_BST(bst.root)
