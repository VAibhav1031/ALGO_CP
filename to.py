n = list(map(int, input().split()))

# condition state that  there will be  x and  y integer where x will of  3 frequencies and  and y will be of 2 freq  this is  the condition for having
# the full house

d = {}

for i in range(len(n)):
    d[n[i]] = n.count(n[i])

c = sorted(list(d.values()))

if c == [2, 2] or c == [1, 3]:
    print("Yes")

else:
    print("No")
