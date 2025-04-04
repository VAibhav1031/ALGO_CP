def maxArea(height):  # max aead , Two  pointer  based problem nice  one
    l_ = 0
    r = len(height) - 1
    total = 0
    while l_ < r:
        # total = max(total, min(height[l], height[r]) * (r - l))
        #
        # if r - l == 1:
        #     return total
        #
        # elif height[l] < height[r]:
        #     for i in range(l + 1, r):
        #         if height[i] > height[l]:
        #             l = i
        #             break
        #
        #         if i == r - l:
        #             return total
        #
        # elif height[l] >= height[r]:
        #     for j in range(r - 1, l, -1):
        #         if height[j] > height[r]:
        #             r = j
        #             break
        #
        #         if j == l + 1:
        #             return total

        current_total = (
            min(height[l_], height[r]) * (r - 1)
        )  #  we choose  the min  because of the difference between the height of the pillars
        # length *breadth of the area   basically nothing else

        total = max(
            total, current_total
        )  # here we choosen the max  which is to return max value between current  and previously calculcated one

        if (
            height[l_] < height[r]
        ):  # here we shift  to  those pillars which are better in height raather being small
            l_ += 1

        else:
            r -= 1

    return total


print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # ans will be  the 49 okay
