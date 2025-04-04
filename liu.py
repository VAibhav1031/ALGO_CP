# def print_n(l_: int):
#     if l_ == 1:  # base condition
#         print(1)
#         return 1
#     print_n(l_ - 1)  # hypothesis
#
#     print(l_)  # induction
#
#
# print_n(9)
#

# now to make  it  in  reverse form
#
# we have  to  change the  hypothesis  like  earlier  it  was  1 to n now it is the n to 1
#
# so  we have  to  print  firsrt  n  then   move on to  next n-1  okay


# def print_n(l_: int):
#     if l_ == 1:  # base condition
#         print(l_)
#         return 1
#
#     print(l_)  # hypothesis
#     print_n(l_ - 1)  # induction
#
#
# print_n(9)

# l_ = {}
#

# def fact(m):
#     if m <= 1:  # base  case  i will say
#         return 1
#     if m in l_:
#         return l_[m]
#     # in  this  we are using fact(m-1) as the hypothesis  but  binding it  to the
#     # fact(m)
#     # like  m* fact(m)  is  the induction
#
#     else:
#         l_[m] = m * fact(m - 1)
#         return l_[m]
#
#
# n = int(input())
# print(fact(n))
#

# Sum of  the  first N natural numbers
# def naturalSum(n: int) -> int:
#     if n == 1:
#         return 1
#
#     return n + naturalSum(n - 1)
#
#
# print(naturalSum(n))
#

# def fibonacci(n: int) -> int:
#     if n == 0: #
#         return 0
#
#     if n == 1 or n == 2: # base condition
#         return 1
#
#     return fibonacci(n - 1) + fibonacci(n - 2)
#
#
# print(fibonacci(n))
#
#
#


# Count the number of digits in a number
#

# count = 0
#
#
# def countDigit(n: int) -> int:
#     if n < 0 or n < 10:
#         return 1
#
#     return 1 + countDigit(n // 10)
#
#
# print(countDigit(157))
#
#


# import sys
#
#
# def reverseString(s: str) -> str:
#     if len(s) <= 1:
#         return s
#
#     return s[-1] + reverseString(s[: len(s) - 1])
#
#
# s = input()
# print(reverseString(s))
#
#
# def computePower(x: int, n: int) -> int:
#     if n == 1:
#         return x
#     return x * computePower(x, n - 1)
#
#
# print(computePower(5, 13))
#
#
# def ispalindrome(s: str, start: int, end: int) -> bool:
#     if start <= end:
#         return True
#
#     if s[start] != s[end]:
#         return False
#
#     return ispalindrome(s, start + 1, end - 1)
#
#
# lk = sys.stdin.readline().strip()
# print(ispalindrome(lk, 0, len(lk)))
#
#
# def sumDigit(nu: int) -> int:
#     if nu < 10:
#         return nu
#
#     return nu % 10 + sumDigit(nu // 10)
#
#
# num = int(input("Enter the  result please : : :: :"))
# print(sumDigit(num))
#


# def convertNumberToBinary(n: int) -> int:
#     if n < 2:
#         return n
#     return convertNumberToBinary(n // 2) * 10 + (n % 2)
#
#
# print(convertNumberToBinary(56))
#

#
# def divisor_of_Number(num: int, d: int = 1):
#     if d > num:
#         return
#
#     if num % d == 0:
#         print(d)
#
#     return divisor_of_Number(num, d + 1)
#
#
# divisor_of_Number(12)
#
#
# def gcd(a, b):
#     if a == 0:
#         return b
#
#     if b == 0:
#         return a
#
#     return gcd(b, a % b)
#
#
# print(gcd(15, 25))
#
#
# def count_occurrenc(num: int, target_digit: int):
#     if num == 0:
#         return 0
#
#     return (1 if num % 10 == target_digit else 0) + count_occurrenc(
#         num // 10, target_digit
#     )
#
#
# print(count_occurrenc(3414, 4))
#
#
# def product_withoutstar(num, num1, d=1):
#     """
#     we have the  number and all hehe hehehehhehehhehe!! hhahahahahahah:::))))))
#     """
#     if d > num:
#         return 0
#
#     return num1 + product_withoutstar(num, num1, d + 1)
#
#
# n, n1 = map(int, input().split())
# print(product_withoutstar(n, n1))
#
#
# def sum_of_element_in_Array(num: list[int]) -> int:
#     if len(num) == 1:
#         return num[0]
#
#     return num[0] + sum_of_element_in_Array(num[1:])
#
#
# print(sum_of_element_in_Array([8, 6, 3]))
#
#
# def maximum_number_array(nums: list[int]) -> int:
#     if len(nums) == 1:
#         return nums[0]
#
#     return max(nums[0], maximum_number_array(nums[1:]))
#
#
# print(maximum_number_array([9, 6, 3, 2, 1, 56, 22, 34]))

#
# import math
# import re
#
#
# def remOccur(s: str, target):
#     if len(s) < len(target):
#         return s
#
#     if s[: len(target)] == target:
#         return remOccur(s[len(target) :], target)
#
#     return s[0] + remOccur(s[1:], target)
#
#
# print(remOccur("abcokbc", "bc"))
#

# def convert_strnum_int(s: str) -> int:
#     if len(s) == 1:
#         return int(s)
#     return convert_strnum_int(s[1:]) * 10 + int(s[0])
#
#
# print(convert_strnum_int("1234"))
#

#
# def convert_strnum_int(s: str) -> int:
#     if len(s) == 1:
#         return int(s)
#     return int(s[0]) * (10 ** (len(s) - 1)) + convert_strnum_int(s[1:])
#
#
# print(convert_strnum_int("1234"))
#
#
# def strcmp(s1: str, s2: str) -> int:
#     if not s1 and not s2:
#         return 0
#
#     if not s1:
#         return -1
#
#     if not s2:
#         return 1
#
#     if s1[0] != s2[0]:
#         return ord(s1[0]) - ord(s2[0])
#
#     return strcmp(s1[1:], s2[1:])
#
#
# print(strcmp("mukf", "muk"))
#
#
# def sqrt_Root_Estimation(num):
#     i = 0
#     j = num
#
#     while i <= j:
#         mid = (i + j) // 2
#         if mid * mid == num:
#             return mid
#
#         if mid * mid < num:
#             i = mid + 1
#
#         else:
#             j = mid - 1
#     return i
#
#
# def power(mid, x, n):
#     res = 1.0
#
#     for _ in range(n):
#         res *= mid
#
#         if res > x:
#             return res
#
#     return res
#
#
# def nth_Root_Estimation(X, N):
#     low, high = 0, X
#
#     precision = 1e-6
#
#     while (high - low) > precision:
#         mid = (low + high) / 2
#
#         r = power(mid, X, N)
#         if r == X:
#             return mid
#
#         if r < X:
#             low = mid + 1
#
#         else:
#             high = mid - 1
#
#     return round(low, 6)
#
#
# print(sqrt_Root_Estimation(81))
#
# print(nth_Root_Estimation(128, 4))
# print(nth_Root_Estimation(81, 2))
#

#
# def generate_subsequence(s: str):
#     # we have  to go with  two choice  pick  and not to  pick
#     #  ok  but  one thing to check   how  to make  thing that like
#     #  BEst way is  to go  around  using the  REcursion tree which is th best choice  i would say for any one
#
#     if not s:
#         return [""]
#
#     subsequence = generate_subsequence(s[1:])
#
#     # Simple   recursion  no  backtracking here okay
#     # simply we  are including the  character  first  and other choice  is  to not  choose the  cuurent  first  character
#     return [s[0] + sub for sub in subsequence] + subsequence
#
#
# print(generate_subsequence("abc"))
#
#
# def strcmp(s1: str, s2: str) -> int:
#     if not s1 and not s2:
#         return 0
#
#     if not s1:
#         return -1
#
#     if not s2:
#         return 1
#
#     if s1[0] != s2[0]:
#         return ord(s1[0]) - ord(s2[0])
#
#     return strcmp(s1[1:], s2[1:])
#

#
# this  will be the way you can get the  function which  will tell the two
# string is being equal or not character by character

#
# def factorial(n):
#     if n <= 1:
#         return 1
#
#     return n * factorial(n - 1)
#
#
# print(factorial(5))
#
#
# def print_ntimes(st: str, n):
#     if n == 0:
#         return
#
#     print(st)
#
#     return print_ntimes(st, n - 1)
#
#
# print_ntimes("hello", 4)
#
#
# def count_Occur(num: list[int], target: int) -> int:
#     if not num:
#         return 0
#
#     if num[0] == target:
#         return 1 + count_Occur(num[1:], target)
#
#     return count_Occur(num[1:], target)
#
#
# print(count_Occur([3, 6, 9, 2, 6, 3, 7, 6], 3))
#
#
# def isSorted(num: list[int]) -> bool:
#     if len(num) <= 1:
#         return True
#
#     return num[0] < num[1] and isSorted(num[1:])
#
#
# print(isSorted([6, 3, 2, 4]))
#
#
# def product_n(n):
#     if 0 < n < 10:
#         return n
#
#     return n % 10 * product_n(n // 10)
#
#
# print(product_n(521))
#
#
# def product_n_1(n):
#     if n <= 1:
#         return 1
#
#     return n * product_n_1(n - 1)
#
#
# print(product_n_1(6))
#
#
# def sum_of_number_digits(num):
#     if 0 < num < 10:
#         return num
#
#     return num % 10 + sum_of_number_digits(num // 10)
#
#
# print(sum_of_number_digits(987))
#
#
# def reverse_number(num):
#     if num < 10:
#         return num
#
#     return num % 10 * (10 ** (len(str(num)) - 1)) + reverse_number(num // 10)
#
#
# def reverse_number1(num):
#     if num < 10:
#         return num
#
#     return num % 10 * (10 ** (int(math.log10(num) - 1) + 1)) + reverse_number(num // 10)
#
#
# print(reverse_number(521))
#
# print(reverse_number(6341))
# print(reverse_number1(528))
# print(reverse_number1(201))
# print(reverse_number1(9409))
#
#
# def countZero(num):
#     if not num:
#         return 0
#
#     if num % 10 == 0:
#         return 1 + countZero(num // 10)
#
#     return countZero(num // 10)
#
#
# print(countZero(3060260460))
#
#
# def number_of_steps_to_reduce_number_to_zero(nym, steps):
#     if nym == 0:
#         return steps
#
#     return (
#         number_of_steps_to_reduce_number_to_zero(nym // 2, steps + 1)
#         if nym % 2 == 0
#         else number_of_steps_to_reduce_number_to_zero(nym - 1, steps + 1)
#     )
#
#
# print(number_of_steps_to_reduce_number_to_zero(14, 0))
#
#
# def isSorted(nums: list[int]):
#     if len(nums) <= 1:
#         return True
#
#     return nums[0] < nums[1] and isSorted(nums[1:])
#
#
# print(isSorted([9, 6, 2, 2]))
#
#
# def linearSearch(nums: list[int], target, index):
#     if nums[0] == target:
#         return index
#
#     return linearSearch(nums[1:], target, index + 1)
#
#
# print(linearSearch([9, 6, 9, 3, 1, 45, 8], 3, 0))
#

# Noice
# def findAll(nums: list[int], target: int, index_: int, lop: list[int]):
#     if index_ == len(nums):
#         return lop
#
#     if nums[index_] == target:
#         lop.append(index_)
#
#     return findAll(nums, target, index_ + 1, lop)
#
#
# print(findAll([6, 7, 3, 2, 4, 3], 3, 0, []))
#
#
# def findAll_new(nums: list[int], target: int, index_):
#     l_ = []
#
#     if index_ == len(nums):
#         return l_
#
#     if nums[index_] == target:
#         l_.append(index_)
#
#     ans = findAll_new(nums, target, index_ + 1)
#
#     return l_ + ans
#
#
# print(findAll_new([6, 7, 3, 2, 4, 3], 3, 0))
#
#
# def rotatedbinarySearch(nums: list[int], low: int, high: int, target: int):
#     if low > high:
#         return -1
#
#     mid = (low + high) // 2
#
#     if nums[mid] == target:
#         print("YYYYAAA!! We hittt the middle")
#         return mid
#
#     if nums[low] < target < nums[mid]:
#         return rotatedbinarySearch(nums, low, mid - 1, target)
#
#     return rotatedbinarySearch(nums, mid + 1, high, target)
#
#
# nums = list(map(int, input().split()))
# print(rotatedbinarySearch(nums, 0, len(nums) - 1, 15))
#

#
# def print_invert_rightTriangle(row: int, col: int):
#     if row == 0:
#         return
#
#     if col < row:
#         print("*", end="")
#         print_invert_rightTriangle(row, col + 1)
#
#     else:
#         print()
#         print_invert_rightTriangle(row - 1, 0)
#
#
# print_invert_rightTriangle(5, 0)
#
#
# def print_invert_rightTriangle1(row: int, col: int):
#     if row == 0:
#         return
#
#     if col < row:
#         print_invert_rightTriangle1(row, col + 1)
#         print("*", end="")
#     else:
#         print_invert_rightTriangle1(row - 1, 0)
#         print()
#
#
# print_invert_rightTriangle1(3, 0)

#
# def bubbleSort(nums: list[int], n: int):
#     if n == 1:
#         return
#
#     for i in range(n - 1):
#         if nums[i] > nums[i + 1]:
#             nums[i], nums[i + 1] = nums[i + 1], nums[i]
#
#     bubbleSort(nums, n - 1)
#
#
# l_ = list(map(int, input().split()))
# bubbleSort(l_, len(l_))
#

#
# print()
#
#
# def bubbleSort1(nums: list[int], row, col) -> None:
#     if row == 0:
#         return
#
#     if col < row:
#         if nums[col] > nums[col + 1]:
#             nums[col], nums[col + 1] = nums[col + 1], nums[col]
#
#         bubbleSort1(nums, row, col + 1)
#
#     else:
#         bubbleSort1(nums, row - 1, 0)
#
#
# l_1 = list(map(int, input().strip().split()))
#
# bubbleSort1(l_1, len(l_1) - 1, 0)
# print(l_1)
#
#
# def tail_recursive_bubble_sort(arr: list[int], n: int, index: int = 0) -> None:
#     # Base case: If we've processed the entire list
#     if n == 1:
#         return
#
#     # If we've reached the end of the current pass, start the next pass
#     if index == n - 1:
#         return tail_recursive_bubble_sort(arr, n - 1, 0)
#
#     # Compare and swap if needed
#     if arr[index] > arr[index + 1]:
#         arr[index], arr[index + 1] = arr[index + 1], arr[index]
#
#     # Tail call: Move to the next index
#     tail_recursive_bubble_sort(arr, n, index + 1)
#
#
# l_1 = list(map(int, input("Enter numbers: ").split()))
# tail_recursive_bubble_sort(l_1, len(l_1))
# print(l_1)


# in the selection Sort we usually use the  largest element and swap it with the last element
# in this we are gonna just  maintain the  max_value index  which will be going to pass every time
# and it gonna change if there will be any bigger element  and  other part will done according to that


# def selectionSort(nums: list[int], row, col, max_):
#     if row == 1:
#         return
#
#     if col < row:
#         if nums[col] > nums[max_]:
#             selectionSort(nums, row, col + 1, col)
#         else:
#             selectionSort(nums, row, col + 1, max_)
#     else:
#         nums[max_], nums[row - 1] = nums[row - 1], nums[max_]
#         selectionSort(nums, row - 1, 0, max_)
#
#
# k = [6, 2, 4, 5, 3]
#
# selectionSort(k, len(k), 0, 0)
#
# print(k)
#


# def merge(nums, nums1, m, n):
#     k = []
#     i, j = 0, 0  # i know  we can  use way better representation using while lop
#
#     while i < m and j < n:
#         if nums[i] < nums1[j]:
#             k.append(nums[i])
#             i += 1
#
#         else:
#             k.append(nums1[j])
#             j += 1
#     #
#     if i < m:
#         k.extend(nums[i:m])
#
#     # while i < len(nums):
#     #     k.append(nums[i])
#     #     i += 1
#
#     if j < n:
#         k.extend(nums1[j:n])
#
#     # while j < len(nums1):
#     #     k.append(nums1[j])
#     #     j += 1
#
#     return k
#

# print(merge([3, 4, 7], [2, 6, 12]))

#
# def merge_sort(arr: list[int], lo, high):
#     if lo == high:
#         return [arr[lo]]
#
#     mid = (lo + high) // 2
#     left = merge_sort(arr, lo, mid)
#     right = merge_sort(arr, mid + 1, high)
#     return merge(left, right, len(left), len(right))
#
#
# arr = list(map(int, input().strip().split()))
# print(merge_sort(arr, 0, len(arr) - 1))
#
#
# def merge_sort_in_place(arr, s, e):
#     if e - s <= 1:
#         return
#
#     mid = (s + e) // 2
#
#     merge_sort_in_place(arr, s, mid)
#     merge_sort_in_place(arr, mid, e)
#
#     merge_in_place(arr, s, mid, e)
#
#
# def merge_in_place(arr, s, m, e):
#     mix = [0] * (e - s)
#
#     i = s
#     j = m
#     k = 0
#
#     while i < m and j < e:
#         if arr[i] < arr[j]:
#             mix[k] = arr[i]
#             i += 1
#
#         else:
#             mix[k] = arr[j]
#             j += 1
#
#         k += 1
#
#     while i < m:
#         mix[k] = arr[i]
#         i += 1
#         k += 1
#
#     while j < e:
#         mix[k] = arr[j]
#         j += 1
#         k += 1
#
#     for l_ in range(len(mix)):
#         arr[s + l_] = mix[l_]
#
#
# arr_ = list(map(int, input().strip().split()))
# merge_sort_in_place(arr_, 0, len(arr_))
# print(arr_)
#
#
def quickSort(num, L, H):
    if L < H:
        j = partition(num, L, H)
        quickSort(num, L, j - 1)
        quickSort(num, (j + 1), H)


def partition(num: list[int], l_: int, h: int):
    p = num[0]
    i = l_
    j = h

    while True:
        while num[i] < p:
            i += 1

        while num[j] > p:
            j += 1

        if i >= j:
            break
        num[i], num[j] = num[j], num[i]

    mid = (l_ + h) // 2
    num[l_], num[mid] = num[mid], num[l_]

    return j


sd = list(map(int, input().split()))
quickSort(sd, 0, len(sd))
