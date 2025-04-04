import math


# t = int(input())
# n = 1
#
#
# while (t):
#     x, y  = list(map(int, input().split()))
#
#     if y % x == 0:
#         print(int((y/x)-1))
#
#
#     else:
#         print(y//x)
#
#
#     t -= 1
#
#


def isPrime(n):
    if n == 1:
        return False

    else:
        for i in range(2, int(math.sqrt(n))):
            if n % i == 0:
                return False
        return True


## Sieve Eratosthenes :
n = int(input())

s = [True] * n

s[0] = s[1] = False

for i in range(2, int(math.sqrt(n)) + 1):
    if s[i]:
        for j in range(i * i, n, i):
            if j % i == 0:
                s[j] = False


print(s)

s1 = [i for i in range(len(s)) if s[i]]
print(s1, len(s1))
