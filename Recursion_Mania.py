# so  we know , what and how the  resursion basically works  but  somehow  every topic has some key points which still
# to bre remembered


# like  in Recursion itself , how the stack is adding up  to  getting small, according to the flow of the  functions
# What are the patterns  we are writing the recursion code , it is something we must know to have good way how it work


# okay  we  are going to find the  particular pattern  files in the directory and  we will  do that using recursion
# and using python for that is little bit joke but yeah if  someone know how it works it will be no that abstracted i would syyyyy

import re
import os


def find_files_matching_pattern(searchPath, pattern, depth):
    """
    Recursively finds and prints files matching the given regex pattern
    starting from a given directory path.
    """

    path = os.path.expanduser(searchPath)
    # this is  the base case where we may get the file
    print(" " * depth + f"->{path}")
    if not os.path.exists(path):
        return
    matche_files = 0
    if os.path.isfile(path):
        match = pattern.search(os.path.basename(path))
        # if pattern.fullmatch(os.path.basename(path)):
        if match:
            print(os.path.basename(path))
            matche_files = 1
        # return   # this thing basically shortening or removing the element from the stack
        # which make the stack to not overflow , but there could be other condtion which can cause problem

    elif os.path.isdir(path):
        for items in os.listdir(path):
            new_path = os.path.join(path, items)
            matche_files += find_files_matching_pattern(new_path, pattern, depth + 1)

    return matche_files


#  we have to only match the  cats named  image file , which are named with cat1.jpg and
# pat = re.compile(r"^[\w\-]+\.\w{2,5}$")
pat = re.compile(r"cat\d+\.jpg")
searchpath = "~/Documents_test"

print(find_files_matching_pattern(searchpath, pat, 0))

# ---------------------------------------ITERATIVE--------------------------------------------------

stack = []
pattern = pat
stack.append({"searchPath": "~/Documents"})
while stack:  # or you can say !stack.empty ,
    frame = stack.pop()
    path = os.path.expanduser(frame["searchPath"])
    if os.path.isfile(path):
        match = pattern.search(os.path.basename(path))
        # if pattern.fullmatch(os.path.basename(path)):
        if match:
            print(os.path.basename(path))

    elif os.path.isdir(path):
        for items in os.listdir(path)[::-1]:
            new_path = os.path.join(path, items)
            stack.append({"searchPath": new_path})
