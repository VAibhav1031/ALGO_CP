for _ in range(int(input())):
    a, b, c = list(map(int, input().split()))

    if a + b >= 10:
        print("YES")

    elif b + c >= 10:
        print("YES")

    elif c + a >= 10:
        print("YES")

    else:
        print("NO")
