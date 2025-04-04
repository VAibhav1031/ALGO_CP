t = int(input())

for _ in range(t):
    n = int(input())

    if 1 <= n <= 20:
        if n <= 5:
            if n % 2 == 0:
                print(n // 2, n // 2)
            else:
                print(n // 2, (n // 2) + 1)

        elif n == 10:
            print(0, 10)
        elif n > 10:
            print((n - 10), 10)
        else:
            print((10 - n), (n - (10 - n)))
