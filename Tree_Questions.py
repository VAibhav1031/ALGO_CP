# print the node level by level 
#
# we have to solve this problem 
# lets do something 
from collections import deque
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None 
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None


    # it will basically print the nodes from left to right at each level by level , by  just getting to know level by level we just use the bfs here 
    #
    # there is one more  modified  similar question comes to  get the average of each level  . simple 
    def levelOrder(self, root):
        if root is None:
            return

        queue = deque([root])
        result = []
        while queue:
            level_size = len(queue)
            current_level = []
            for _ in range(level_size):
                curr_node = queue.popleft()
                current_level.append(curr_node.value)
                if curr_node.left:
                    queue.append(node.left)

                if curr_node.right:
                    queue.append(node.right)


            result.append(current_level)


        return result



    #  now we have to print the successor of the node 
    #
    def levelOrderSuccessor(self,root,succ):
        if root is None:
            return None
        
        if  root == succ:
            if root.left:
                return root.left

            if root.right:
                return root.right

            
            else:
                return None

        queue = deque([root])
        
        # here no operations is done  on the same level so we are not  using the for loop ,  dont get panick  why there is no  for loops 
        # The thing is  we just  want the next of the required node , it doesnt matter of having on same level can be on next level  so there is no need we can use for loop
        # which only harness operations on the same level ....!!!
        while queue:
            level_size = len(queue)
            curr_node = queue.popleft()

            if curr_node.left:
                queue.append(curr_node.left)

            if curr_node.right:
                queue.append(curr_node.right)

            if curr_node == succ:
                break


        return queue[0]


    
    # in this  we just have 
    # Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values. (i.e., from left to right, level by level from leaf to root).
    # simple  as fuck ,  just we have to reverse the result what we did the in first part
    def levelOrder_Second(self, root):
        if root is None:
            return

        queue = deque([root])
        result = []
        while queue:
            level_size = len(queue)
            current_level = []
            for _ in range(level_size):
                curr_node = queue.popleft()
                current_level.append(curr_node.value)
                if curr_node.left:
                    queue.append(node.left)

                if curr_node.right:
                    queue.append(node.right)


            result.append(current_level)


        return result[::-1]




    def rightSideView(self, root):
        if not root:
            return []

        results = []

        queue = deque([root])
        while queue:
            level_size = len(queue)

            for i in range(level_size):
                curr_node = queue.popleft()

                if i == level_size-1:
                    results.append(curr_node.value)

                if curr_node.left:
                    queue.append(curr_node.left)

                if curr_node.right:
                    queue.append(curr_node.right)



        return results



    def symmetric(self, root):

        # in this  we basically want to  know whether the  binary tree is the symmetric/mirror , more in layman way palindrome ,
        # they just want to know like  if we  fold the paper  both side will show equality ,  mirror for
        # you can check the leetcode symmetric question very easy just few thing to know 
        #
        # so  we dont add the root , there is no need for that  we first add the its left and right 
        # we will check both thing , are they have anomaly or not , if not we will move and 
        # add the  both  end /edges  
          #      1
          #    /   \
          #   2     2
          #  / \   / \
          # 3   4 4   3

        # so in this we  have  to  check  whethere both tree edges are same not , like we use to do in palindrome
        # lets take example - "arora"   fir  "a" from first and last  yes same then move inside check both again 
        #
        # same we have to do here  
        #
        # how we add them  , we are gonna add the left and right node of root and always check validity then we will add the elements 
        # first  two last edges then  there inner edges 
        # [not2,not2,3,3,4,4] ,  here not2  means  they are popped and then only it will proceed and add them 

        queue = deque()
        queue.append(root.left)
        queue.append(root.right)

        while queue:
            left = queue.popleft()
            right = queue.popleft()

            if left is None and right is None:
                continue

            if left is None or right is None:
                return False 

            if left.value != right.value:
                return False


            queue.append(left.left)
            queue.append(right.right)
            queue.append(left.right)
            queue.append(right.left)


        return True

        

if __name__ == "__main__":


    ## Test Cases of the levelOrderSuccessor
    # root = Node(20)
    # root.left = Node(10)
    # root.left.left = Node(4) 
    # root.left.right = Node(18) 
    # root.right = Node(26)
    # root.right.left = Node(24) 
    # root.right.right = Node(27) 
    # root.left.right.left = Node(14) 
    # root.left.right.left.left = Node(13) 
    # root.left.right.left.right = Node(15)
    # root.left.right.right = Node(19)
    #
    # key = root.right.left # node 24 
    #
    # bt = BinaryTree()
    # res = bt.levelOrderSuccessor(root, key) 
    #
    # if res: 
    #     print("LevelOrder successor of " +
    #              str(key.value) + " is " +
    #              str(res.value)) 
    #
    # else:
    #     print("LevelOrder successor of " +
    #           str(key.value) + " is NULL")
    

    ## Test case of the rightview of BinaryTree
    
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = None
    root.left.right = Node(5)
    root.right.left = None
    root.right.right = Node(4)


    bt = BinaryTree()
    print(bt.rightSideView(root))





    










    


    
