n, k = list(map(int, input().split()))
y = list(map(int, input().split()))
c = 0

for i in y:
    if i <= (5 - k):
        c += 1


print(c // 3)
