#  MAximum  sum  of the subarray


# Brute Force  and  optimal  on  the same  way
def maximumSumSubarray(nums: list[int]):

    # n = len(nums)
    # max_sum = float('-inf')
    # curr_sum = 0
    # for i in range(n):
    #     for j in range(i, n):
    #         curr_sum = sum(nums[i:j+1])
    #         max_sum = max(curr_sum, max_sum)
    #
    #
    # if  we got the  subarray where there is no negative integer
    # then just written whole array sum

    return sum(nums)


def minimumSumSubarray(nums: list[int]):

    n = len(nums)
    min_sum = float('inf')
    curr_sum = 0
    for i in range(n):
        for j in range(i, n):
            curr_sum = sum(nums[i:j+1])
            min_sum = min(curr_sum, min_sum)

    return min_sum

# contains negative and positve integers
# we gonna  make use of sliding window


def maxSumSubarray(nums: list[int]):
    n = len(nums)
    max_sum = float('-inf')
    start = 0
    temp_start = 0
    end = 0
    curr_sum = 0
    for i in range(n):
        curr_sum += nums[i]

        if curr_sum > max_sum:
            max_sum = curr_sum
            start = temp_start
            end = i

        if curr_sum < 0:
            curr_sum = 0
            temp_start = i+1

    return max_sum, nums[start:end+1]


# n = list(map(int, input().split()))
# print(maxSumSubarray(n))
#


def maxSumSubarrayAtleastK(nums: list[int], k):
    n = len(nums)
    current_sum = 0
    for i in range(k):
        current_sum += nums[i]
    prev_sum = 0
    idx = 0
    res = current_sum
    for i in range(k, n):
        current_sum += nums[i]
        prev_sum += nums[idx]
        idx += 1
        res = max(current_sum, res)

        if prev_sum < 0:
            current_sum -= prev_sum
            res = max(res, current_sum)
            prev_sum = 0
    return res


n = list(map(int, input().split()))
k = int(input())
# m = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# print(maxSumSubarray1(m, 3))
print(maxSumSubarrayAtleastK(n, k))
