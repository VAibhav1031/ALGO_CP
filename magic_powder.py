def max_cookies(n, k, a, b):
    low = 0
    # Calculate a more reasonable upper bound
    # high = min((b[i] + k) // a[i] for i in range(n)) + 1
    high = 0
    for i in range(n):
        high = max(high, (b[i]+k)//a[i])
    result = 0

    while low <= high:
        mid = (low + high) // 2

        # Calculate the required magic powder
        required_powder = 0
        for i in range(n):
            needed = a[i] * mid
            if needed > b[i]:
                required_powder += (needed - b[i])

        # If the magic powder is enough, try for more cookies
        if required_powder <= k:
            result = mid
            low = mid + 1
        else:
            high = mid - 1

    return result

if __name__ == "__main__":
    import sys
    # Read the first line (n and k)
    n, k = map(int, sys.stdin.readline().split())
    # Read the second line (a1, a2, ..., an)
    a = list(map(int, sys.stdin.readline().split()))
    # Read the third line (b1, b2, ..., bn)
    b = list(map(int, sys.stdin.readline().split()))

    print(max_cookies(n, k, a, b))