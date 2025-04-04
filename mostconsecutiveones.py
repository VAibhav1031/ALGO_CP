# it will be as the other but will be just using 1
#


def mostConsecutiveOnes(nums: list[int], k) -> int:
    n = len(nums)
    start = 0

    for end in range(n):
        k -= 1 - nums[end]

        if k < 0:
            k += 1 - nums[start]

            start += 1

    return end - start + 1


print(mostConsecutiveOnes([1, 0, 1, 1, 0], 1))
