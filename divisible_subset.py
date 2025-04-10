for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    store = {0: 0}
    s = 0
    # think of  it  we are using the prefix sum which is one of the best thing in dealing with the subarray part of thing where we have
    #
    for i in range(len(a)):
        s = (s + a[i]) % n
        if s in store:
            ans = range(store[s] + 1, i + 2)
            break

        store[s] = i + 1

    print(len(ans))
    print(*ans)
