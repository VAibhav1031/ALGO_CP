def solve():
    l_ = []

    n, m = map(int, input().split())
    for i in range(n):
        el = list(map(int, input().split()))
        l_.append(el)

    ans = 0

    for i in range(n):
        for j in range(m):
            sum = l_[i][j]
            x = j - 1
            y = j + 1

            for k in range((i - 1), -1, -1):
                if x >= 0:
                    sum += l_[k][x]
                    x -= 1

                if y < m:
                    sum += l_[k][y]
                    y += 1

            x = j - 1
            y = j + 1

            for k in range((i + 1), n):
                if x >= 0:
                    sum += l_[k][x]
                    x -= 1

                if y < m:
                    sum += l_[k][y]
                    y += 1

            if sum > ans:
                ans = sum

    print(ans)


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        solve()
