# so we  are writing the test script
from  tree_manifest import BST

bst = BST()


# Insert 1 to 1000
for i in range(1, 1001):
    bst.insert(i)
    # debug purpose
    print("root node: ", bst.root.value)  #
    print("current :", bst.inorder())

print("Tree Size Before Deletion:", len(bst.inorder()), bst.inorder())
print("Tree Height Before Deletion:", bst.height_bst(bst.root))


# currently commenting  for debug related
for i in range(1,1001):
    print("Before delete : ")
    print("inorder_list: ", bst.inorder())
    print("height: ", bst.height_bst(bst.root))

    bst.delete_value(i)

    print("After delete : ")
    print("inorder_list: ", bst.inorder())
    print("height: ", bst.height_bst(bst.root))
