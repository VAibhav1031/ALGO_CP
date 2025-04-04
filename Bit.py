# Bitwise operation

# Left Shift -->  generally multiply the number by  2^k  k  the number of  bits you are shifting to
# it basically add the  number of  0's at last

# where as the  right Shift --> show  use the thing num >> k   which represents shifting the  number to right
# or  removing the number of k bits from  right
#
# or  we can  say it  basically dividing the numebr by the 2^k  floor  values


#  here &  represnt  1 if both true else 0
#  here | (or) represent if one of them is true --> 1  else 0
#  ^ it is  a  xor  based operation

# bitwise operators  are most important  thing to  make  calculation or arithmetic  thing faster  because  of there way working on each bit
# in earlier  computer having the low computing power , computation of any values in normal  way may be  heavy  taskk but  the  bitwise  make thing
# better at that  by interacting to the bit  dirrectly  nowday it is  also good  but  you willl not find too much difference in performance
# because the advancement of the computation power of cput nowdays many cpu can  carry or process to much instruction than  earlier their data piplenes
# are more and faster
#
# but still using bit in  complex and  very time consuming is far  better i will say


# lets  check  out with addition of the two numbers
# num = 5
# num1 = 8
#
#
# basically when you see addition in the binary
#
# 1 0 0 1
# 0 0 1 1
# -------
# 1 1 0 0

# def bitwise_add(a, b):
#     while b != 0:
#         carry = a & b
#         a = a ^ b
#         b = carry << 1
#
#     return a
#
#
# print(bitwise_add(num, num1))
#
#
# print(5 << 4)
# print(5 | 4)


# the thing come  up  to our  mind  is the bit manipulation it is not any formula
# it is  the thing we will say using it  maybe  good or not  upto u

# lets start a bit something baby

# we have to change 2 bit to 1
# we are gonna using |


# this is also called the setting up  to the 1 (from 0) Turning it on
# 5 ->101
# we changed the  2 bit
# 1 << 1 will give us 010
# and performing this on that will give  change the 2 bit

# *****************************************
# print()
# a = int(input())
# print(bin(a))
# print("This is gomma for setting up means Turning on ")
# print("Which bit you wann set you can chooseee  last bit to most bit  0 to n ")
# 2^ 0   for  last bit or 1st bit and   2^ 1  for 2 bit
# n = int(input())
# print(a | (1 << n))
# print(bin(a | (1 << n)))
# print()
# *******************************************
#

# # to Turn of  any bit or  removing the 1
# #  we will gonna use  the & ~
# # **************************************
# a = int(input())
# print(bin(a))
# print("This is gonna for clearing or removing 1 from desired bit pos ")
# print("Which bit you wann set you can chooseee  last bit to most bit  0 to n ")
# # 2^ 0   for  last bit or 1st bit and   2^ 1  for 2 bit
# n = int(input())
# print(a & ~(1 << n))
# print(bin(a & ~(1 << n)))
# print()
# #****************************************


#  #  we can also use  the XOR  for  toglling like we use to do in or bit different
#  # we can use to check  whether this bit is 1 or 0
#  # ***********************************************
#  a = int(input())
#  print(bin(a))
#  # for this  we  gonna use the and & to check if it 1 or 0  if it is 1 will return 1 else 0
#  n = int(input("Enter the bit position to check if it is  1 or not"))
#  print(a & (1 << n) != 0)
#  print(bin(a & (1 << n)))
#  print()
#  #************************************************

# # lets  see some real thing problem
# #
# # check if  a number is odd or even
# #
# # if it is odd it will gonna return 1 at lsb
# # even it will '0'
# #
# # *********************************************
# def is_odd(n):
#     return (n & 1) == 1
#
#
# print(is_odd(5))
# #***********************************************

#
# #  finding the unique
# #  we use the XOR  which will cancel out same  number  and  store  if  it is 0 [same bit will be cancel  out and  different will be counted]
# #  basically think like if  the  number  already  occur and  coming again  it  will be cancel  out  and  only that number  will be there who
# #
# #**************************************
# def finding_unique(n: list[int]):
#     res = 0
#
#     for num in n:
#         res ^= num
#
#     return res
#
#
# print(finding_unique([2, 3, 2, 4, 4]))
# #**************************************

# check if a nmber is  a power of two
# To check  if the number is  the power of th  two  we can say  like  there Most significant  bit is  only 1 else all bits are 0
# so  complement of them  will result in  just -1  value
# ()
#
#
# 8 1000 7 0111  will give 0 will
import math


def is_powertTwo(n):
    return n > 0 and (n & (n-1)) == 0


num = int(input("Enter the number : "))
print(is_powertTwo(num))


def powerSet(num):
    n = len(num)
    subset = []
    for mask in range(1 << n):
        s = [num[i] for i in range(n) if mask & (1 << i) != 0]
        subset.append(s)

    return subset


print(powerSet([1, 2, 3]))


# you have to  basically return  the  which bit   position is set
# lets take  an example of the power of 2


def whichbitSet(num):
    if num & (num-1) != 0:
        return -1  # they are not power of 2number

    return int(math.log2(num)) + 1  # if it is a  power of 2 number


print(whichbitSet(num))


# or if you want to know the x bit of the number if it is 1 or 0

def toKnow(n, x):
    return (n >> (x-1)) & 1


N = int(input("Enter : "))
X = int(input("ENTTTTER"))
print(toKnow(N, X))
