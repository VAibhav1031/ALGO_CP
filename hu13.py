#  we
#  ITs  like in  the  sorted array rotated  one the  minimum element is  between the  two  boundary one is  bigger  than  it  and other less than latter
#  30 40 50 10 20    3040 50  is greater and  20 is  smaller than latter  and 10 is between  them  we  always  say it is less than the last element
#  so  move  the  right =  mid - 1  to more  smaller  element  slowly  converge to  like  area or element or index
from typing import List


def minsortedArray(arr: List[int]):
    lo = 0
    hi = len(arr) - 1
    boundary_ = -1

    while lo <= hi:
        mid = (hi + lo) // 2
        if arr[mid] <= arr[-1]:
            boundary_ = mid
            hi = mid - 1

        else:
            lo = mid + 1

    return boundary_


if __name__ == "__main__":
    n = list(map(int, input().split()))
    print(minsortedArray(n))
