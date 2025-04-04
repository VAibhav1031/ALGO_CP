# t = int(input())
# while t:
#     n, a, b, c = list(map(int, input().split()))
#     def run(n, a, b, c):
#         d = 3
#         su = a + b + c
#
#         if n in [a, b, c]:
#             return 1
#             
#         elif su>=n:
#             return 3
#     
#         elif (a == 1 and b == 1 and c == 1):
#             return n
#         else:
#             while True:
#                 if su<=n:
#                     for i in [a, b, c]:
#                         su += i
#                         d+=1
#                         if su>=n:
#                             # print(su)
#                             return d
#                            
#                 else:
#                     break
#     
#     
#     print(run(n, a, b, c))
#
#     t-=1
#

'''
    PAtterns 
'''

'''
    1.
           ****
           ****
           ****
           ****

'''

# solution :
# n = int(input())
# for i in range(n):
#     print('*'*n)
#n


'''
    2.
           ****
           *  *
           *  *
           ****

'''


# solution



# for i in range(4):
#     if i == 1:
#         print('*','','*')
#     elif i == 2:
#         print('*','','*')
#     else:
#         print('*'*4)
#
#

# BEst  code for any value 
# n = int(input())
# if n>2:
#     
#     for i in range(n):
#         if i == 0:
#             print('*'*n)
#         elif i == n-1:
#             print('*'*n)
#         else:
#             print('*',' '*(n-4),'*')
# else:
#     print("Number should be greater than 2")
#    


'''
    3.
           ****
            ****
             ****
              ****

'''


# solution

# n = int(input())
# for i in range(n):
#     print(' '*i,'*'*n)
#


'''
    4. 
           ****
          ****
         ****
        ****
'''

#  it is  same  as  the  above  one   just  mirrored one of that (rhombus)
# we have  just  rn the loop in  reverse  order  because mirrored  is   the reverse or opposite of  any thing



# n = int(input())
#
# for i in range(n,-1,-1):
#     print(' '*i,'*'*n)


'''
    5.
           *
           **
           ***
           ****
'''
# solution
# n = int(input())
# for i in range(1,n+1):
#     print('*'*i)
#


'''
    6.
              *
             ***
            *****
           *******
'''


# solution


# i Think this  will gonna  be PAtent because of  a such a unique way doing this and removing coercsion

# n = int(input())
#
# for i in range(n):
#     if i == n-(n//2):
#         break
#     print(' '*((n//2)-i),'*'*(2*i+1),' '*((n//2)-i))


#  One  of the  advance  one  of  that  with  no  thinking of  giving the odd  number  to get the  desired  result 
#  Just  give  the  value  for  the Number of  the rows  you want 
# n = int(input())

# for i in range(n):
#     if i == n:
#         print("*"*(2*i+1))
#     print(" "*((n//2)-i+1)+"*"*(2*i+1))
#


'''
    7.
              *
             * *
            *   *
           *******
'''

#solution
# n = int(input())
#
# for i in range(n):
#
#     if i == 0 or i == n-1:
#         print(' '*(n-i-1),'*'*(2*i+1),' '*(n-i-1))
#
#     else:
#
#         print(' '*(n-i-1),'*'+' '*(2*i-1)+'*',' '*(n-i-1))
#
#



'''
    8.
           *******
            *****
             ***
              *
'''

# for i in range(n,-1,-1):
#     print(' '*(n-i),'*'*(2*i-1),' '*(n-i))
#



'''
    9.
           *******
            *   *
             * *
              *
'''

# for i in range(n, -1, -1):
#     if i == 0 :
#          print(' '*(n-i-1),'*'*(2*i+1),' '*(n-i-1))
#
#     elif i == n:
#          print(' '*(n-i-1),'*'*(2*i+1),' '*(n-i-1))
#
#     else:
#         print(' '*(n-i-1),'*'+' '*(2*i-1)+'*',' '*(n-i-1))
#
#



'''
    9.
           *
           **
           ***
           ****
           ***
           **
           *
'''
# n = int(input())
# for i in range(1,n+1):
#     if i >(n//2)+1:
#         print("*"*((n-i)+1))
#     else:
#         print("*"*i)
#
# print()
#
#

# Little Different Waya


# print()
# for i in range(n//2+2):
#     print("*"*i)
#
# for j in range(n//2, -1, -1):
#     print("*"*j)
# 

'''
    10.
        Reverse of uppper one  pattern
'''


# Now  Reverse  of  the  half diamond
# n = int(input())
# for i in range(n):
#     print(" "*((n-i)-1)+"*"*(i+1))
#
# for i in range(n, -1, -1):
#     print(" "*((n-i)+1)+"*"*(i-1))
# 

'''
    11.
             *
            ***
           *****
          *******
           *****
            ***
             *
'''

# Solution : 
#
# n = int(input())
# n2 = int(input())
# for i in range(n):
#     if i == n:
#         print("*"*(2*i+1))
#     print(" "*((n//2)-i+1)+"*"*(2*i+1))
#
#
#
# for i in range(n2-1, -1, -1):
#     print(" "*(n2-i)+"*"*(2*i-1))
#
#


'''
    12.
           1111
           1111
           1111
           1111
'''

#Solution :
# n = int(input())
# for i in range(n):
#     print("1"*n)


'''
    13.
           1111
           2222
           3333
           4444
'''

#Solution : 
# n = int(input())
#
# for i in range(n):
#     print(f"{i+1}"*n)
#


'''
    14.
           333
           313
           323
           333
'''
# Solution : 
# n = int(input())
# for i in range(n-1):
#     if i == 0:
#         print("3"*(n-1))
#     print(f"3{i+1}3")
#

'''
    15.
           1
           23
           456
           78910
'''

# Solution

# n = int(input())
# num = 1  # Initialize the number to be printed
#
# for i in range(1, n + 1):  # Loop for each row (1 to n inclusive)
#     for j in range(i):      # Loop to print numbers in the current row
#         print(num, end="") # Print the current number without a newline
#         num += 1          # Increment the number for the next print
#     print()              # Print a newline to move to the next row
#
#

'''
    16.
           10987
           456
           32
           1
 '''
# n = int(input())
# num_1 = 10
# for i in range(n,-1,-1):
#     for j in range(i):
#         print(num_1, end = "")
#         num_1 -= 1 
#     print()
#
#

'''
    17.
           6666
           555
           44
           3
'''
# import math
# n = int(input())
# num = 6 
# for i in range(n, -1, -1):
#     print(f"{int(math.fabs(num))}"*i)
#
#     num -= 1

#main
# n = int(input())
# num = 6 
# for i in range(n, -1, -1):
#     print(f"{num}"*i)
#
#     num -= 1
#


'''
    18.
           3
           44
           555
           6666
'''

# n = int(input())
# num = 3
# for i in range(n):
#     print(f"{num}"*(i+1))
#     num +=1
#

'''
    19.
           3
           4 5
           6 7 8
           9 10 11 12
'''

n = int(input())
num = 3 
for i in range(n+1):
    for j in range(i):
        print(num, end = " ")
        num += 1 
    print()
