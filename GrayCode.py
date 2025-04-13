# lets soleve  this  mf

# Given a number N, generate bit patterns from 0 to 2^N-1 such that successive patterns differ by one bit.
# A Gray code sequence must begin with 0.


# Example 1:
# # Input:
# N = 2
# Output:
# 00 01 11 10
# Explanation:
# 00 and 01 differ by one bit.
# 01 and 11 differ by one bit.
# 11 and 10 also differ by one bit.


# Example 2:
#
# Input:
# N=3
# Output:
# 000 001 011 010 110 111 101 100
# Explanation:
# 000 and 001 differ by one bit.
# 001 and 011 differ by one bit.
# 011 and 010 differ by one bit.
# Similarly, every successive pattern
# differs by one bit.


# Your task:
# You don't need to read input or print anything. Your task is to complete the
# function graycode() which takes an integer N as input and returns a list of
# patterns.
#
# Expected Time Complexity: O(2n)
# Expected Auxiliary Space: O(2n)

# Constraints :
# 1<=N<=16


#######################
# WAY OF SOLVING
######################


#  first  there is thing we should know that the  Gray Code  ,it is  binary number but succesive number have only one bit  difference
#  as in example  it is given 01 11   here you will see there is only one  bit  difference

### First way : ###
# to know there is a formula  to solve it
# we have the formula  which is  the :::
# [ (Current Binary number) XOR (Current Binary number) >> 1 ]
#
# Example :
# 001 XOR (001)>>1   you will get to know how it  happens will get the result
#
#
# But for this you must know the binary number advance  so  , for this  way of solving you must  create binary number first
# then create the binary and do which still good  but not nice for me
#


### Second Way :: ##

## Recursive ##

# here simple  reflection play important role
# At  n = 1 there will be [0,1]
# for n = 2  you will reverse the og list [1,0]
# now you will have two  list one is  og and other its  reflection :
# [0,1] (OG) , [1, 0] (mirror/reflected one)
#
# preappend 0 at the og  and prepend 1 in mirror  and concatenate
#
# [00,01] and [11,10] ----> [00,01,11,10] gotcha


class Solution:
    def graycode(self, n):
        if n == 1:
            return ["0", "1"]

        prev = self.graycode(n - 1)
        return ["0" + i for i in prev] + ["1" + i for i in prev[::-1]]


s = Solution()

print(s.graycode(3))
