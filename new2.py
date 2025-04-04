def solve():
    n, x = map(int, input().split())

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    co = []
    for i in range(n):
        co.append(A[i] * B[i])

    co.sort(reverse=True)

    su = 0
    c = 0
    for j in range(n):
        su += co[j]
        c += 1

        if su >= x:
            break

    if su >= x:
        print(c)

    else:
        print(-1)


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        solve()


#  So simple  don't  make  thing complex try  to analyze  anything come  to your  even it is vague  at that  moment
#  put it  on the pen paper  and analyze the thing  okay
#  Practice  a lot  okay  you will gonnna do  better  my   broooouuu..
