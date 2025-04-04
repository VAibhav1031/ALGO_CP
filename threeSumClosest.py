def threesumClosest(nums, target: int) -> int:
    n = len(nums)
    nums.sort()
    if n < 3:
        return 0
    closest_sum = float("inf")

    for k in range(n - 2):
        i, j = k + 1, n - 1

        while i < j:
            current_sum = nums[k] + nums[i] + nums[j]

            if abs(target - current_sum) < abs(target - closest_sum):
                closest_sum = current_sum

            if current_sum > target:
                j -= 1

            elif current_sum < target:
                i += 1

            else:
                return target

    return closest_sum


print(threesumClosest([-1, 2, 1, -4], 1))
