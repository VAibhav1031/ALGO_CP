# we  are gonna  make  3sum


def twoSum(target: int, i: int, j: int, nums, result):
    while i < j:
        if nums[i] + nums[j] > target:
            j -= 1
        elif nums[i] + nums[j] < target:
            i += 1
        else:
            while i < j and nums[i] == nums[i + 1]:
                i += 1
            while i < j and nums[j] == nums[j - 1]:
                j -= 1
            result.append([-target, nums[i], nums[j]])
            i += 1
            j -= 1


def threeSum(nums):
    result = []

    n = len(nums)
    target = 0

    nums.sort()
    if n < 3:
        return []
    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        target = 0 - nums[i]

        twoSum(target, i + 1, n - 1, nums, result)

    return result


print(threeSum([-1, 0, 1, 2, -1, -4]))
