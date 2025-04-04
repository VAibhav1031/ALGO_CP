n = int(input())

for i in range(n, -1, -1):
    t = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # so here the main logic where should i think how to give mini
    sum_ = 0
    i_ = 0
    if sum(x*y for x, y in zip(a, b)) >= t[1]:
        # for i in range(len(a)):
        #     for j in range(len(b)):
        #         sum_ += a[i]*b[j]
        #         i_ += 1
        #     if sum_ >= t[1]:
        #         print(i)
        #         break
        for i in a:
            for j in b:
                sum_ += i*j
                i_ += 1
            if sum_ >= t[1]:
                print(i_)
    else:
        print(-1)
