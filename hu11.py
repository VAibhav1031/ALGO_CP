def firstNotSmallerThanTarget(arr, target):
    lo = 0
    hi = len(arr) - 1
    boundary_ = -1

    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] > target:
            boundary_ = mid
            hi = mid - 1

        else:
            lo = mid + 1

    return arr[boundary_]


if __name__ == "__main__":
    n = list(map(int, input().split()))
    target = int(input())
    print(firstNotSmallerThanTarget(n, target))
