def isValid(arr, coworker, max_pages):
    co_worker_count = 1
    current_sum = 0

    for newtime in arr:
        if newtime > max_pages:
            return False

        if current_sum + newtime > max_pages:
            co_worker_count += 1
            current_sum = newtime
            if co_worker_count > coworker:
                return False
        else:
            current_sum += newtime

    return True


def mintimeNeswpaper(arr, co):
    lo = max(arr)
    hi = sum(arr)
    result = -1

    while lo < hi:
        mid = (lo + hi) // 2
        if isValid(arr, co, mid):
            result = mid
            hi = mid - 1

        else:
            lo = mid + 1

    return result


if __name__ == "__main__":
    n = list(map(int, input().split()))
    co_worker = int(input())
    print(mintimeNeswpaper(n, co_worker))
