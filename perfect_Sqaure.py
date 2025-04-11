def numSquare(n):
    sqaures = []

    i = 1
    while i * i <= n:
        sqaures.append(i * i)
        i += 1

    def dfs(target):
        if target == 0:
            return 0

        if target < 0:
            return float("inf")

        minsquares = float("inf")

        for sqaure in sqaures:
            if sqaure > target:
                break

            minsquares = min(minsquares, 1 + dfs(target - sqaure))

        return minsquares

    return dfs(n)


print(numSquare(12))
