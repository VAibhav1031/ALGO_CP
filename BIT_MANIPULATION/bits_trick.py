# here we goo ,

# first  thing
# Swap  the the two number without using the third variable

# we mostly use XOR(TOggle one)
# here the explaination
# a = a^b  XOR basically did the toggling effect for same bits [101 ^ 110 => 011]
# b = a^b  , now  here a is  already (a = a^b)  we know  a^a  == 0  (same bit will give 0)
# --->  result b == (a^b)^b  with distirbutive property we will get the b == a  [011^110 => 101]
# now do  the thing with a again
# a ^=b  ---> a ==b [011^101 ==> 110]
#
a = 5
b = 6
print(a, b)
a ^= b
b ^= a
a ^= b

print(a, b)
# -----------------------------------------
# Check if ith bit is  set or not
# we mostly use shifts and And operator

n = 13
i = 2
# here i is the position
if (a & (1 << i)) != 0:
    print(f"{bin(a & (1 << i))}SET")
else:
    print("NO")


# Here we can right shift also
if (a & (a >> 2)) == 0:
    print("Hurray ")
else:
    print("Bhurray")


# -------------------------------------------
# to  set a bit at some position simple use the OR |

n = 13  # 1101 is the binary
i = 1
print(bin(n | (1 << i)))

# -------------------------------------------
# clearing the ith bit
# in this we mainly use two things
# lets say  we have  the 1101 we have to clear the i = 2 position bit


#  let say we have
#  1<<2 => 0b100 mainly na , then we have 1101  & 0100  will give if the bit at that position is set or not
#  if  we  do ~(1<<2)  --> 011  , if  we have 8 bit integer it looks something like this  11111011 ,
#  now lets do  the  00001101 & 11111011  will give 00001001, or mainly 1001
#
#  so the formula is  to use n & ~(1<<i)
#


n = 13  # 1101
i = 2  # clearing bit position
result = bin(n & ~(1 << i))

print(result)

# --------------------------------------------
# Toggle the ith bit ,  toggle in the sense
# 1101 if  you have to change 0 to 1  you mainly use
#
# 1-1  --> 0  1-0 --> 1

# for smaller version it can be mixed ly usedf by other things
n = 13  # 0b1101
print(n ^ (1 << 2))
print(bin(n ^ (1 << 2)))

# ---------------------------------------------
# REmove the last SEt bit(Rightmost)
# if  we have to remove the rightmost SEt bit for any binary things we use this mostly usefull
# n & (n-1)  you will know  why it is helpful, like if i say there is n = 16 1000 n = 15 is 0111 , check  there 2^i position power
# They power reduces by 1 which make the rightmost SET  bit to  0 and  all bits righ to SET  bit 1
# try you will get to know  more

n = 13
print(n & (n - 1))


# ---------------------------------------------
# Count the number of power of 2 , (dont get confused ,  it is basically 2^n ,  similarly if someones say 4 power of n ,means n^4)

# mainly all power of 2 has only one  SET bit which is at MSB position if we count that binary  set only, else it is the leftmost position

# 16 -- 1000  , 32  -- 10000
n = 16
if (n & (n - 1)) == 0:
    print("Yes")
else:
    print("NOOO")


# count the number of Set bits
#
# let say we divide the
# n = 13
# n /= 2 13 1
# n /= 2 6 0
# n /= 2 3 1
# n /= 2 1 1

# count = 0
# while n>1:
#     if n % 2 == 1:
#         count += 1
#
#     n /= 2
#
# print(count)
# we use the n%2  for checking odd(because they only give the 1 as remainder)
# bitwise way is n&1 101 & 001 --> yes
# why only lsb is checked for the odd , n = 7  in binary  2^2(4) + 2^1(2) + 2^0(1)  this one is always at the last of any odd you pick

count = 0
while n > 1:
    count += n & 1
    n /= 2

print(count)

# time complexity , log(n)

# --------------------------------
# we can  improve it more  by using the concept o the clearing Rightmost SET bit
# which can reduce complexity to  O(number of Rightmost set bit
c = 0
while n != 0:
    count += n & (n - 1)
    n /= 2

print(c)
