# n = int(input())
# for _ in range(n):
#    n_1 = input()
#    if len(n_1) >= 10:
#        print(f'{n_1[0]}{len(n_1) - 2}{n_1[-1]}')
#    else:
#        print(n)


def sqrtx(x):
    if x <= 1:
        return x
    for i in range(x):

        if x == 2:
            return 1

        elif i*i > x:
            return i-1


n = int(input("Enter the number (sqrt using the brute one "))
print(sqrtx(n))


# brute but   still nice  cuz its   time coplexity  is sqrt(x) || it always  go to the i+1  thing meanin if you  go with 625 it will
# go to 26 * 26  then it  will return i-1 which is  25
# so work perfect  square very well
# and  for   non-perfect square it will  give round of it
#


# def bS(x):
#    l_ = 0
#    r = x
#    while (l_ <= r):
#        mid = (l_ + r)//2
#        if mid * mid > x:
#            r = mid - 1

#        elif mid * mid < x:
#            l_ = mid + 1

#        else:
#            return mid

#    return r


# print(bS(7))
#
#
# this  is is the one of the best with   large number  cuz it is  a O(log n)


# now  we  have  to  calculate the pow (x, n ):
#  okay there is some thing  we have to check like
#
#  for the the negative numbers :
# Example 1:

# Input: x = 2.00000, n = 10
# Output: 1024.00000
#
# Example 2:
#
# Input: x = 2.10000, n = 3
# Output: 9.26100
# 00, n = -2
# Output: 0.25000
# Explanation: 2-2 = 1/22 = 1/4 = 0.25

# so here it is :
#
#
# def pow(x, n):
#     return x**n


x = float(input("Enter the number : "))
n = int(input("Enter the power : "))
# print(pow(x, n))

# we are gonna  see different appraoch


def pow(x, n):
    x_ = 1
    if n > 0:
        for _ in range(n):
            x_ *= x
        return x_
    else:
        for _ in range(n):
            x_ *= x
        return (1/x_)


print(pow(x, n))
