# array of  integers numes  sorted  non-decreasing order, find the starting and  ending position
# of given target value
# if target isn't  found you must  written [-1,-1]


def starEnd(arr, target):
    lo = 0
    hi = len(arr) - 1
    res = -1
    while lo <= hi:
        mid = (hi + lo) // 2
        if arr[mid] == target:
            res = mid
            break
        if arr[mid] > target:
            hi = mid - 1

        else:
            lo = mid + 1

    if res != -1:
        return [res, res + 1]

    else:
        return [-1, -1]


if __name__ == "__main__":
    n = list(map(int, input().split()))
    targ = int(input())
    print(starEnd(n, targ))
