# in this  we are gonna  represent  the counting sort
# we will have the array  and  then we will create  the counter of that
# aftr that  then  we will do the running sum/ cummulative sum of it  which will represent the place
# where the
#

#
# def countingSort(arr):
#     k = max(arr)
#
#     count = [0] * (k + 1)
#
#     for i in range(len(arr)):
#         for j in range(len(count)):
#             if arr[i] == j:
#                 count[j] += 1
#
#     # cummulative sum
#     for i in range(1, len(count)):
#         count[i] += count[i - 1]
#
#     og = [0] * len(arr)
#     for j in range(len(arr) - 1, -1, -1):
#         count[arr[j]] = count[arr[j]] - 1
#         index = count[arr[j]]
#         #  i think  the  problem  here  we  are getting is  the   count  is not  updating
#         #  earlier  we were  not  doing the update in the count  list which was  causing overwriting the placed  element
#         og[index] = arr[j]
#
#     return og
#
#
#


def countingSort(arr):
    k = max(arr)  # Maximum value in the array
    min_val = min(arr)  # Minimum value in the array

    # Create the count array
    count = [0] * (k - min_val + 1)

    # Populate the count array
    for num in arr:
        count[num - min_val] += 1

    # Compute cumulative sum in count array
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Create the output array
    og = [0] * len(arr)

    # Place elements in the correct position
    for j in range(len(arr) - 1, -1, -1):
        index = count[arr[j] - min_val] - 1
        og[index] = arr[j]
        count[arr[j] - min_val] -= 1  # Update the count array

    return og


if __name__ == "__main__":
    n = list(map(int, input().split()))
    print(countingSort(n))
