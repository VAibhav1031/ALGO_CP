# def countingSort(nums: list[int]):
#     n_ = len(nums)
#     # i think  the best part is that we must have the
#     k = max(nums)
#     d = [0] * (k + 1)
#
#     output = [0] * n_
#
#     for i in range(n_):
#         d[nums[i]] += 1
#
#     # the most  important part is  the running sum :
#     for i in range(1, len(d)):
#         d[i] += d[i - 1]
#
#     # placing elements to its required place
#     for i in reversed(nums):
#         d[i] -= 1
#         output[d[i]] = i
#
#     return output
#

# print(countingSort([8, 9, 6, 3, 5, 10]))


def countingSortForRadix(nums: list[int], exp):
    # now you will just need count of size 10 but  why the reason is simple because in radix we will gonna sort the numbers according
    # to the the places like  first we aplly it one  ones , then tens ... soe on  so every place  doesnt  containg more than 9
    # and follow  decimal number  system which is said that we just goonna maintain the  size of 10 ,

    # the problem the countingSort face is been removed  by using countingSort only  like  whenever we had bigger element in the array
    # using counting sort we need to creat max_ele+1 length of array , yeah i know that will be constant  but  constant still matters
    # ammortized analysis which on easy understand is removed also play important role on runtime of your code .....

    # Count array (running sum) plays major  role for  just telling where the actual location of the value will be
    # we always  go from last  in original array while placing the value in output are for maintaining the stability of duplicate elements
    # let's goo

    n_ = len(nums)

    output = [0] * n_
    count = [0] * 10

    for num in nums:
        index = (num // exp) % 10
        count[index] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for num in reversed(nums):
        index = (num // exp) % 10

        count[index] -= 1

        # output[count[index]-1] = num  we have already decremented the value in count  so no necessary doing again will cause defunctioning of sort
        #  if  we have  made the  assignment  earlier  than decrement of value in count  , then only we can use it
        output[count[index]] = num

    for i in range(n_):
        nums[i] = output[i]


def isSorted(arr):
    return all(arr[i] < arr[i + 1] for i in range(1, len(arr) - 1))


def isReverse(arr):
    return all(arr[i] > arr[i + 1] for i in range(1, len(arr) - 1))


def radixSort(arr):
    # if sorted(arr) == arr:
    #     return arr
    #
    # if arr == sorted(arr)[::-1]:
    #     return arr[::-1]
    #
    # These are good but  we  are using the sorted() function which is  like  n(logn) way bad for large array , we could do way better

    # Now  these are way better just o(n) and we get to know are they reverse or sorted , which will save lot of time  and computation power
    if isSorted(arr):
        return arr
    if isReverse(arr):
        arr[:] = arr[::-1]

        return arr

    exp = 1
    max_ = max(arr)

    while max_ // exp > 0:
        countingSortForRadix(arr, exp)
        exp *= 10

    return arr


if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(radixSort(arr))
    print(radixSort([123, 456, 789, 12, 34, 56, 7, 89, 9]))
