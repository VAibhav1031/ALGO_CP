for _ in range(int(input())):
    n = input()
    s = list(n)
    s1 = [int(i) for i in s]

    if sum(s1[:3]) == sum(s1[3:]):
        print("YES")

    else:
        print("NO")
