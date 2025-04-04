# we are gonna   do this
#

# 1004. Max Consecutive Ones III
# Medium
# Topics
# Companies
# Hint
#
# Given a binary array nums and an integer k, return the maximum number of consecutive 1's
# in the array if you can flip at most k 0's.
#
#
#
# Example 1:
#
# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
#
# Example 2:
#
# Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
# Output: 10
# Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
#
#
#
# Constraints:
#
#     1 <= nums.length <= 105
#     nums[i] is either 0 or 1.
#     0 <= k <= nums.length
#


# we are gonna make  something better here see

# brute Force approach here :
#
# *******************************
# def maxconsecutiveOnes(nums, k):
#     n = len(nums)
#     max_ = float("-inf")
#     for i in range(n):
#         for j in range(i, n):
#             if nums[i: j + 1].count(0) <= k:
#                 max_ = max(max_, j - i + 1)
#
#     return max_
#
#
# print(maxconsecutiveOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))
# print(maxconsecutiveOnes([0, 0, 1, 1, 0, 0, 1,
#       1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3))
#
# ****************************************


# Optimal approach :

# i think  we
#
#
# from collections import defaultdict


def maxconsecutiveOnes(nums, k):
    n = len(nums)
    start = 0
    zero_count = 0
    ma = float("-inf")
    for end in range(n):
        if nums[end] == 0:
            zero_count += 1

        while zero_count > k:
            if nums[start] == 0:
                zero_count -= 1
            start += 1
        ma = max(ma, end - start + 1)

    return ma


print(maxconsecutiveOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))
