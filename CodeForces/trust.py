#  First  required  thing is  to  have the
# we have  the price of the  drink  in every shop
# we must sort prices  of every shopt   and  check (using binary search) which one  is   having  price of  drink less than equal  to the i th day money he have


import sys

n = int(sys.stdin.readline().strip())
price_n = list(map(int, sys.stdin.readline().strip().split()))

q = int(sys.stdin.readline().strip())
price_n.sort()
for _ in range(q):  # this is the number of the consecutive days he gonna drink
    money_ith_day = int(sys.stdin.readline().strip())  # every day his budget
    lo = 0
    hi = n - 1  # we will gonna check this  for  n number of shops
    # binary search to check  whethere today  he gonna able  to  get the  coffee from  any shop with today budget
    while lo <= hi:
        mid = (lo + hi) // 2

        if price_n[mid] > money_ith_day:
            hi = (
                mid - 1
            )  # if the  current shop price for drink is greater than budget move to smaller bdget one

        else:
            lo = (
                mid + 1
            )  # if the current shop price is  equal or less than current which is good , we are moving mid+1 in desire to get more

    print(lo)  # lo will at the place where with current budget user can buy a coffe
