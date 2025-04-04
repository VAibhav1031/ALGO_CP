# Sum triangle from array
# Last Updated : 16 Nov, 2022
#
# Given an array of integers, print a sum triangle from it such that the first level has all array elements. From then, at each level number of elements is one
# less than the previous level and elements at the level is be the Sum of consecutive two elements in the previous level.
# Example :
#
#
# Input : A = {1, 2, 3, 4, 5}
# Output : [48]
#          [20, 28]
#          [8, 12, 16]
#          [3, 5, 7, 9]
#          [1, 2, 3, 4, 5]
#
# Explanation :
# Here,   [48]
#         [20, 28] -->(20 + 28 = 48)
#         [8, 12, 16] -->(8 + 12 = 20, 12 + 16 = 28)
#         [3, 5, 7, 9] -->(3 + 5 = 8, 5 + 7 = 12, 7 + 9 = 16)
#         [1, 2, 3, 4, 5] -->(1 + 2 = 3, 2 + 3 = 5, 3 + 4 = 7, 4 + 5 = 9)
#

# solution :

# okay
#
# def sumTriangle(arr):
#     if len(arr) < 1:
#         return
#
#     ar = []
#     for i in range(len(arr) - 1):
#         ar.append(arr[i] + arr[i + 1])
#
#     sumTriangle(ar)  # every call will be returned
#     print(
#         arr
#     )  # we will gonna print the arr because thats what function thinking of getting and change to
#
#
# sumTriangle([1, 2, 3, 4, 5])
#

# Recursive Programs to find Minimum and Maximum elements of array
# Last Updated : 19 Sep, 2023
#
# Given an array of integers arr, the task is to find the minimum and maximum element of that array using recursion.
#
# Examples :
#
# Input: arr = {1, 4, 3, -5, -4, 8, 6};
# Output: min = -5, max = 8
#
# Input: arr = {1, 4, 45, 6, 10, -8};
# Output: min = -8, max = 45
#
# Recursive approach to find the Minimum element in the array
#

# solution

#
# def findMinMax(arr, min_, max_):
#     if len(arr) < 1:
#         print(f"min = {min_}, max = {max_}")
#         return
#
#     if arr[0] > max_:
#         max_ = arr[0]
#
#     elif arr[0] < min_:
#         min_ = arr[0]
#
#     findMinMax(arr[1:], min_, max_)
#
#
# findMinMax([1, 4, 45, 6, 10, -8], float("inf"), -float("inf"))
# findMinMax([1, 4, 3, -5, -4, 8, 6], float("inf"), -float("inf"))


# First uppercase letter in a string (Iterative and Recursive)
# Last Updated : 09 Dec, 2022
#
# Given a string find its first uppercase letter
# Examples :
#
# Input : geeksforgeeKs
# Output : K
#
# Input  : geekS
# Output : S
#
# Method 1: linear search
# Using linear search, find the first character which is capital


# def firstUpperCase(stri: str):
#     if len(stri) < 1:
#         return
#
#     if 65 <= ord(stri[0]) <= 90:

# print(chkPRime(4))


# # power of TWO :
#
#
# def powerOfN(num, exp):
#     if exp <= 1:
#         return num
#
#     if exp % 2 == 0:
#         return powerOfN(num, exp // 2) * powerOfN(num, exp // 2)
#
#     return num * powerOfN(num, exp // 2) * powerOfN(num, exp // 2)
#
#
# num, exp = map(int, input().split())
# print(powerOfN(num, exp))
#

#
#    Write a recursive function for given n and a to determine x:

# n = a ^ x
# a = 2, 3, 4
# (2 ^ -31) <= n <= (2 ^ 31) - 1

#
# def determine(n, a, c):
#     if 0 < n < 1:
#         c += 1
#         return determine(n * a, a, c)
#     if abs(n - 1.0) < 1e-9:
#         return c
#
#     if n % a != 0:
#         return -1
#
#     c += 1
#     return determine(n / a, a, c)
#
#
# n = float(input("Enter the n : "))
# a = int(int(input("Enter the a: ")))
#
# if 0 < n < 1:
#     print(-(determine(n, a, 0)))
# else:
#     print(determine(n, a, 0))

#
# # Check if the  array is  sorted or not recursively
#
# #
# def isSorted(nums):
#     if len(nums) == 1:
#         return True
#
#     if nums[0] > nums[1]:
#         return False
#
#     return isSorted(nums[1:])
#
#
# j = list(map(int, input().split()))
# print(isSorted(j))
#

# check  number of  steps  to reduce to the 0

#
# def reduceToZero(num):
#     if num == 0:
#         return 0
#
#     c = 1
#     if num % 2 == 0:
#         c += reduceToZero(num // 2)
#
#     else:
#         c += reduceToZero(num - 1)
#     return c
#
#
# n = int(input("Enter the thing ::"))
# print(reduceToZero(n))
#

# parenthesis Checker:
# Yes! You can solve the Valid Parentheses problem using recursion. The idea is to recursively process the string by removing valid pairs of brackets and checking if the remaining string is valid.
# Recursive Approach
#
#     Find the first occurrence of a closing bracket.
#
#     Check if the preceding character is its corresponding opening bracket.
#
#     If yes, remove the pair and recursively check the rest of the string.
#
#     If at any point the condition is violated, return False.
#

#
# def parenthesisChecker(org: list[str], strii: str):
#     if not strii and not org:
#         return True
#
#     if not strii and org:
#         return False
#
#     matching = {"}": "{", ")": "(", "]": "["}
#
#     # basically here we are checking the  thing of last in org and then  current string first in the dictionary
#     if strii[0] in matching:
#         if org and org[-1] == matching[strii[0]]:  # Check for matching pair
#             org.pop()
#             return parenthesisChecker(org, strii[1:])
#         else:
#             return False
#
#     org.append(strii[0])
#     return parenthesisChecker(org, strii[1:])
#
#
# print(parenthesisChecker([], "[()(]{}"))
#
#
# def parenthesisChecker(strii: str):
#     matching = {"}": "{", ")": "(", "]": "["}
#     org = []
#
#     def helper(index: int):
#         if index == len(strii):
#             return not org
#         # basically here we are checking the  thing of last in org and then  current string first in the dictionary
#         if strii[index] in matching:
#             if org and org[-1] == matching[strii[index]]:  # Check for matching pair
#                 org.pop()
#                 return helper(index + 1)
#             else:
#                 return False
#
#         org.append(strii[index])
#         return helper(index + 1)
#
#     return helper(0)
#
#
# print(parenthesisChecker("[()()]{}"))
#
#


# REmove duplicates


# def removeDuplicates(process: str, strii: str):
#     if not strii:
#         return process
#
#     if strii[0] in process:
#         return removeDuplicates(process, strii[1:])
#
#     else:
#         process += strii[0]
#         return removeDuplicates(process, strii[1:])
#

# print(removeDuplicates("", "ababaabb"))


# now  the task is not  to use  the process variable in the function must be inside

#
# def removeDuplicates(strii: str):
#     if not strii:
#         return ""
#
#     if strii[0] in strii[1:]:
#         return removeDuplicates(strii[1:])
#
#     return strii[0] + removeDuplicates(strii[1:])
#
#
# print(removeDuplicates("aabaa"))
#


# import math
#
#
# def removeConsecutiveDuplicates(strii: str):
#     if len(strii) == 1:
#         return strii
#
#     if strii[0] == strii[1]:
#         return removeConsecutiveDuplicates(strii[1:])
#
#     return strii[0] + removeConsecutiveDuplicates(strii[1:])
#
#
# print(removeConsecutiveDuplicates("aabb"))
#

# memeoryoptimized
# print all pallindromic partition of the string


# def pallindromicString(strii: str):
#     if not strii:
#         return True
#
#     if strii[0] != strii[-1]:
#         return False
#
#     return pallindromicString(
#         strii[1:-1]
#     )  # because here we  have  the  string being the immutable , it is impossible  for me  to create memory ruckus
#

# def pallindromicString1(strii: str, left: int, end: int):
#     if left >= end:  # empty
#         return True
#
#     if strii[left] != strii[end]:
#         return False
#
#     return pallindromicString1(strii, left + 1, end - 1)
#
#
# print(pallindromicString("nitin"))
# print(pallindromicString1("nitn", 0, len("niin") - 1))
#

##
# def pallindromicStringPartition(strii: str, left: int, right: int, path, result):
#     if left > right:  # Base case: reached the end
#         result.append(path[:])  # Store a copy of the valid partition
#         return
#
#     for i in range(left, right + 1):  # Iterate over partition points
#         if pallindromicString1(strii, left, i):
#             # Include current palindrome substring
#             path.append(strii[left: i + 1])
#             pallindromicStringPartition(
#                 strii, i + 1, right, path, result)  # Recur
#             path.pop()  # Backtrack
#
#     return result
#
#
# print(pallindromicStringPartition("nitin", 0, len("nitin") - 1, [], []))
#

# power SEt:
#
# "abc" -->  {a} {b) {c} {ab} {ac} {bc} {abc}


# def powerSet(process: str, strii: str):
#     if not strii:
#         print(process)
#         return
#
#     powerSet(process + strii[0], strii[1:])
#     powerSet(process, strii[1:])
#
#
# powerSet("", "abc")
#


#  combination Sum
#
#  [2,3,6,7] target  = 7
#  [[2,2,3],[7]]
#
#  so we have to return the list of  list  containing the elements whose sum are wqual tot the target
#  We can take  more than  element from the array
#  we must  use backtraking to  backtrack  and  sum  the  thing
#


def combinationSum(candidate: list[int], target: int):
    result = backtracking(candidate, [], [], target, 0)

    return result


def backtracking(nums, result, temp_list, remain, start):
    if remain < 0:
        return

    if remain == 0:
        result.append(temp_list[:])
        return
    for i in range(start, len(nums)):
        temp_list.append(nums[i])
        # we are not  doing i+1  cause of  taking same element
        backtracking(nums, result, temp_list, remain - nums[i], i)
        temp_list.pop()

    return result


print(combinationSum([2, 3, 6, 7], 7))


def wordSearch(grids: list[list[str]], word: str):
    rows, cols = len(grids), len(grids[0])

    def backtrack(row, col, index):
        if index == len(word):
            return True

        if (
            row < 0
            or row >= rows
            or col < 0
            or col >= cols
            or grids[row][col] != word[index]
        ):
            return False

        temp, grids[row][col] = grids[row][col], "#"

        result = (
            backtrack(row - 1, col, index + 1)
            or backtrack(row + 1, col, index + 1)
            or backtrack(row, col - 1, index + 1)
            or backtrack(row, col + 1, index + 1)
        )

        grids[row][col] = temp
        return result

    for i in range(rows):
        for j in range(cols):
            if backtrack(i, j, 0):
                return True
    return False


print(
    wordSearch(
        [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"
    )
)


def targetSum(nums, target):
    def backtrack(nums, current_sum, target, index, mem):
        if (index, current_sum) in mem:
            return mem[(index, current_sum)]
        if index == len(nums):
            if current_sum == target:
                return 1

            else:
                return 0

        count = 0

        count += backtrack(nums, current_sum + nums[index], target, index + 1, mem)
        count += backtrack(nums, current_sum - nums[index], target, index + 1, mem)

        mem[(index, current_sum)] = count
        return mem[(index, current_sum)]

    return backtrack(nums, 0, target, 0, {})


print(targetSum([1, 1, 1, 1, 1], 3))
