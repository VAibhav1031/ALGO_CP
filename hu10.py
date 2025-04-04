#  this  is  the  something you must  see  and  try  to  do  okay Related  to  the  Binary Search

# def firstOcurrenceTrue(arr):
#     lo = 0
#     hi = len(arr) - 1
#     boundary_ = -1
#     while lo < hi:
#         mid = (lo + hi) // 2
#
#         if arr[mid]:
#             boundary_ = mid
#             hi = mid - 1
#
#         else:
#             lo = mid + 1
#
#     return boundary_
#
#
# if __name__ == "__main__":
#     n = [x == "true" for x in input().split()]
#     res = firstOcurrenceTrue(n)
#     print(res)
#


# different--------------------------------

# def lastOcurrenceFalse(arr):
#     lo = 0
#     hi = len(arr) - 1
#     boundary_ = -1
#     while lo <= hi:
#         mid = (lo + hi) // 2
#
#         if arr[mid]:
#             hi = mid - 1
#
#         else:
#             boundary_ = mid
#             lo = mid + 1
#
#     return boundary_
#
#
# if __name__ == "__main__":
#     n = [x == "true" for x in input().split()]
#     res = lastOcurrenceFalse(n)
#     print(res)
#

# different--------------------------------

#  you  have  given the sorted  array and  have  to  find  the  target value firstOcurrenceb things okay
#  like  you have  given  4 3 5 6 2 5 1 2  target = 5 so  array  must have  to be the  sorted  one  which
#  will  help  in using binary search because then only the array would be the  monotonic


# in this  we  will gonna  use  some  different  approach  like  target  can be  less adn  above the mid  so


def firstOcurrenceTarget(arr, target):
    lo = 0
    hi = len(arr) - 1
    boundary_ = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            boundary_ = mid
            hi = mid - 1

        elif arr[mid] < target:
            lo = mid + 1

        else:
            hi = mid - 1

    return boundary_


if __name__ == "__main__":
    n = list(map(int, input().split()))
    target = int(input())
    print(firstOcurrenceTarget(n, target))
