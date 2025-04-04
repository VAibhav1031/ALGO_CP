# Given an array of integers arr, return the number of subarrays with an odd sum.
#
# Since the answer can be very large, return it modulo 109 + 7.
#
#
#
# Example 1:
#
# Input: arr = [1,3,5]
# Output: 4
# Explanation: All subarrays are [[1],[1,3],[1,3,5],[3],[3,5],[5]]
# All sub-arrays sum are [1,4,9,3,8,5].
# Odd sums are [1,9,3,5] so the answer is 4.
#
# Example 2:
#
# Input: arr = [2,4,6]
# Output: 0
# Explanation: All subarrays are [[2],[2,4],[2,4,6],[4],[4,6],[6]]
# All sub-arrays sum are [2,6,12,4,10,6].
# All sub-arrays have even sum and the answer is 0.
#
# Example 3:
#
# Input: arr = [1,2,3,4,5,6,7]
# Output: 16
#
#
#
# Constraints:
#
#     1 <= arr.length <= 105
#     1 <= arr[i] <= 100


# even + even = even
# odd + odd = even
# odd + even  = odd
# even + odd = odd
#
#
# so in the prefix_sum if the sum comes odd then there must some  prefix[i-1] which is even because of that we get this
#
# 5 + 6 = 11 (odd)
# 5 - 6 = -1 (odd)
#
#
# sum(i,j) = prefix[j]-prefix[i-1]
# in this way if  prefix[j] -- > odd then  prefix[i-1] must be even to get the  odd result
def numberOfSubarrays(nums: list[int]) -> int:
    n = len(nums)
    count = 0
    even_count = 1
    odd_count = 0
    prefix_sum = 0
    for i in range(n):
        prefix_sum += nums[i]
        if prefix_sum % 2 == 1:
            count += even_count
            odd_count += 1

        else:
            count += odd_count
            even_count += 1

    return count


# i think  sliding window  will fail  miserably because here we dont  want any

if __name__ == "__main__":
    n = list(map(int, input().split()))
    print(numberOfSubarrays(n))
