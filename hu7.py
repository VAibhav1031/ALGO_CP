#  we  are  gonna  make  subarray sum divisible  by k

# BRute Force


# def divisibleByk(arr, k):
#     result = 0
#     for i in range(len(arr)):
#         for j in range(i, len(arr)):
#             n = sum(arr[i : j + 1])
#             if n % k == 0:
#                 result += 1
#
#     return result
#
#
# if __name__ == "__main__":
#     arr = list(map(int, input().split()))
#     k = int(input())
#     print(divisibleByk(arr, k))
#


#  little  bit   improvement  can  be  made  by using the prefix  sum  or  cummulativesum array
#
#  for  example if  we have  the  array : > 2 1 4 3
#  0 2 3 7 10 then  if   we   want  the  sum of  subarray [1, 4, 3]  here in og array i = 1  & j = 3
#  so  formula would be  cumsum[j] - cumsum[i-1] if  i ==0  then simply return cumsum[j]
#


# def divisibleByk(arr, k):
#     result = 0
#     cum_sum = [0] * (len(arr) + 1)
#     cum_sum[1:] = arr
#
#     for i in range(1, len(cum_sum)):
#         cum_sum[i] += cum_sum[i - 1]
#
#     for i in range(len(arr)):
#         for j in range(i, len(arr)):
#             su = cum_sum[j] if i == 0 else cum_sum[j] - cum_sum[i - 1]
#
#             if su % k == 0:
#                 result += 1
#
#     return result
#
#
# if __name__ == "__main__":
#     ar = list(map(int, input().split()))
#     k = int(input())
#     print(divisibleByk(ar, k))
#
#  This is O(n^2)  okay


# now   comes  the best  optimal  one with only o(n)
from collections import defaultdict


def divisibleByk(arr, k):
    result = 0
    cum_sum = [0] * (len(arr) + 1)
    cum_sum[1:] = arr

    for i in range(1, len(cum_sum)):
        cum_sum[i] += cum_sum[i - 1]

    freq = defaultdict(int)
    freq[0] = 1

    for i in range(1, len(cum_sum)):
        rem = cum_sum[i] % k
        if rem < 0:
            rem += k

        if rem in freq.keys():
            result += freq[rem]
        freq[rem] += 1

    return result


if __name__ == "__main__":
    n = list(map(int, input().split()))
    k = int(input())
    print(divisibleByk(n, k))
