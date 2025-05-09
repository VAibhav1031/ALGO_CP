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





    
        

if __name__ == "__main__":


    ## Test Cases of the levelOrderSuccessor
    root = Node(20)
    root.left = Node(10)
    root.left.left = Node(4) 
    root.left.right = Node(18) 
    root.right = Node(26)
    root.right.left = Node(24) 
    root.right.right = Node(27) 
    root.left.right.left = Node(14) 
    root.left.right.left.left = Node(13) 
    root.left.right.left.right = Node(15)
    root.left.right.right = Node(19)
 
    key = root.right.left # node 24 
    
    bt = BinaryTree()
    res = bt.levelOrderSuccessor(root, key) 
 
    if res: 
        print("LevelOrder successor of " +
                 str(key.value) + " is " +
                 str(res.value)) 
     
    else:
        print("LevelOrder successor of " +
              str(key.value) + " is NULL")




    










    


    
