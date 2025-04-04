import sys


# def nonDecreasingSubarray(l:[int]):
#     lu = []
#     for i in range(len(l)):
#         temp = [l[i]]
#         for j in range(i+1,len(l)):
#             if l[j-1]<l[j]:
#                 temp.append(l[j])
#             else:
#                 break
#         lu.append(temp)
#     
#
#     op = []
#     for k in range(len(l)):
#         remp = [l[k]]
#         for m in range(k+1,len(l)):
#             if l[m-1]>l[m]:
#                 remp.append(l[m])
#
#             else:
#                 break
#         op.append(remp)
#     
#
#     # return lu,op
#     lu_ = max(lu, key = len)
#     op_ = max(op, key = len)
#     if len(op_) > len(lu_):
#          return len(op_)
#
#     else:
#          return len(lu_)
#     
#   

def longestmonotonicSubarray(nums : [int]):
    temp_count = 1 
    max_v = 1 

    for i in range(1,len(nums)):
        if nums[i]>nums[i-1]:
            temp_count+=1 
            max_v = max(temp_count,max_v)

        else:
            temp_count  = 1 

    temp_count = 1 
    for i in range(1,len(nums)):
        if nums[i]<nums[i-1]:
            temp_count += 1 
            max_v = max(temp_count,max_v)

        else:
            temp_count = 1 

    return max_v
l = list(map(int, sys.stdin.readline().strip().split()))
print(longestmonotonicSubarray(l))
print(longestmonotonicSubarray([10, 20, 30, 40, 50, 5, 15, 25, 35, 45, 1, 11, 21, 31, 41, 2, 12, 22, 32, 42, 3, 13, 23, 33, 43, 4, 14, 24, 34, 44, 5, 15, 25, 35, 45, 6, 16, 26, 36, 46, 7, 17, 27, 37, 47, 8, 18, 28, 38, 48]))
