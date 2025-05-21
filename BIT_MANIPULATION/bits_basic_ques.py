import math
# so yeah In this  i mostly go with the basic Question , that will help me to get the basic idea of the Bits working

# 1.Minimum bits to flip to get to the goal

start = 10  # 1010
goal = 7  # 0111

# now  we have to
# 1101
# yes, yes ,no, yes
# so  we have  change the first bit and then no change in second and then change
# in all


# how  do we achieve this we can by using the most important thing is XOR ,
# which helps in toggling the same bit

# 1010 ^ 0111 --> 1101  so  this  value came now you will say  we didnt  get
# the 7,the goal is to find the Minimum number of bits to flip to get the things to 7
# and the result accompanying all those bits we have to flip to get the goal ,
# which is mainly answer ,
#
# NOw  we just have to count the number of set bits
#
# which is done by the & operator , but we have to go with one which tell which bit is set


# ----------------------------------------------------------------------------------------------
# powerset
# using bits manipulation
#
# so  yeah  what is the power set:  [1,2,3] --> [1], [2], [3], [1,2], [2,3],[1,2,3],[]


# so  how  we can go and use the  bits manipulation here ,
# first thing  the formula for the number of powerset in it ,  2^n where n is the number of element in the list

# lets  say  we have
#         [1, 2 , 3]
# position  0  1   2


# we can use the same position in bits table
# for  n = 3 ,there will be 8

# 2 1 0
# -----
# 0 0 0 --> []
# 0 0 1 --> [1], 1 is at the 0th position
# 0 1 0 --> [2]
# 0 1 1 --> [1, 2]
# 1 0 0 --> [3]
# 1 0 1 --> [1, 3]
# 1 1 0 --> [2, 3]
# 1 1 1 --> [1, 2, 3]

# 1 -> is for taking that position, we use that position to create the subset and all
# 0 -> for skippping


def powerset(lis):
    n = len(lis)
    ans = []
    for k in range(1 << n):
        l_ = []
        for i in range(n):
            if k & (1 << i):
                l_.append(lis[i])
        ans.append(l_)

    return ans


print(powerset([1, 2, 3]))


# --------------------------------
# single number_1
# in this basically you will have the duplicates of the number (means freq:2)
# and there will be one element which doesnt you must return that
# You can do it with the map one, i.e dictionary in the python
# but still it would be slow for bigger ones
ni = [4, 1, 2, 1, 2]
n = len(ni)
xor = 0
for i in range(n):
    xor ^= ni[i]


print(xor)

# ---------------------------------
# SingleNumber_2
#  find the single number when you have the three same repeated  number not two ,
#  now  why it is different because XOR only work if there are two same then  0 will be answer
#  but here there will be different thing

# now
# let do this
# map  version

# count the frequencies and return the one which is  with one  ,
# Simple no problem , time complexxity is still not that good .


#  [5, 5, 5, 6, 4, 4, 4]
#  what we can  make here is  that we can  make table of these values
#  2 1 0
#  -----
#  1 0 1
#  1 0 1
#  1 0 1
#  1 1 0
#  1 0 0
#  1 0 0
#  1 0 0


# here what you are seeing is bit  different is  like what we can do ,
# we have made  table  and all now we have three ocurrences of number'
# so yeah , we have to use the thing like we have three ocurrence  then
# repeated bits will have multiple of 3 in that position
# if  it has  then we wont count that, we only count which is not
# because that position will story the set bit of the non repeated one

#
# if someone is using static type of language then please give the range according the lenght of datatype, int --> 32 bits
# but we have no choice, i think why soo ,

ans = 0
nums = [5, 5, 5, 6, 4, 4, 4]
n = len(nums)
max_bits = int(math.log2(max(nums))) + \
    1 if nums else 1  # At least 1 bit for safety
for bit_index in range(max_bits):
    count = 0
    for i in range(n):
        if nums[i] & (1 << bit_index):
            count += 1

    if count % 3 == 1:
        ans = ans | (1 << bit_index)


print(ans)


# we can make it bit more  bettter
# by sorting , and  breaking/measurely  returning when the condition like  right and left not equal  something like
# that else it gonna  be  the lst element

# [2, 2, 1, 2, 1, 1, 4, 3, 4, 4]
# [1,1,1,2,2,2,3,4,4,4]

# simple one loop and if some condition in  the loop  comes True, it will return that thing
nums = [2, 2, 1, 2, 1, 1, 4, 3, 4, 4]
nums.sort()


def sol_2(num):
    for i in range(n, 3):
        if num[i] != num[i - 1]:
            return num[i - 1]

    return nums[-1]


print(sol_2(nums))

# we have few  twicely  repeated  numbers  , but  there are  two such numbers
# which are repeated so we haev to get them

s = [2, 4, 2, 3, 14, 7, 7, 3]
xor = 0
for i in range(len(s)):
    xor ^= s[i]

b1, b2 = 0, 0
rightmost = (xor & (xor - 1)) & xor
for i in range(len(s)):
    if rightmost & s[i]:
        b1 ^= s[i]

    else:
        b2 ^= s[i]

print([b1, b2])
