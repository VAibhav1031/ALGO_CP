#  find the maximum sum subarray of  fixed  size given by question,
#


def fixedsizesubarraymaxSum(nums, size):
    # [-1, 2, 3,1,-3, 2]
    # d = {}

    # we  will not  use  this  because  we  already have  given  the size of  the subarray which is fixed not increasing
    # just simple  thing is  that you must  use one loop which will keep window of given size
    #
    # for i in range(len(nums)):
    #     for j in range(i,len(nums)):
    #         d[nums[i:j+1]]= sum()  # this part at moment can make  thing worse to  o(n^3) which woooooooooorseee!!
    #

    # for i in range(len(nums) - 1):
    #     d[i] = nums[i:size]
    #     size += 1
    #
    # return d[
    #     max(d, key=lambda k: sum(d[k]))
    # it  might be  loook like this  but sometime it isn't  that what you thing

    # this  will still gonna  to the o(n^2) because we are assigning the valye  and all

    n = len(nums)
    max_sum = float(
        "-inf"
    )  # sometimes  we use this   because if  the  max subarray sum maybe there is 0  only
    max_subarray = []

    current_sum = sum(nums[:size])

    if current_sum > max_sum:
        max_sum = current_sum
        max_subarray = nums[:size]

    for i in range(size, n):
        current_sum += nums[i] - nums[i - size]  #  Dynamic  fixed size sliding window
        if current_sum > max_sum:
            max_sum = current_sum

            max_subarray = nums[i - size + 1 : i + 1]

    return max_subarray

    # basically we have  to go about the size and   which is  given  us and fixed


print(fixedsizesubarraymaxSum([-1, 2, 3, 1, -3, 2], 3))
