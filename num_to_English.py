###
# Convert a non-negative integer num to its English words representation.
#
#
#
# Example 1:
#
# Input: num = 123
# Output: "One Hundred Twenty Three"
#
# Example 2:
#
# Input: num = 12345
# Output: "Twelve Thousand Three Hundred Forty Five"
#
# Example 3:
#
# Input: num = 1234567
# Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
#
#
#
# Constraints:
#
#     0 <= num <= 231 - 1
#


#  first  thought came to my mind  for  solving this  thing is like  use something with the  dwictionatu and  hard code  and  will do
#  but  now  we must  divide it into the  chunks   i would  say   will be  the  better

# no  i would say  it  is  something which would be like
#
# 123456   123 456  ---> 123 (thousands) & 456 (units)
#
# one  hundred three thousand   four hundred  fifty six


def process(part):
    if not part:
        return

    a_ = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
    }
    ties = {
        20: "Twenty",
        30: "Thirty",
        40: "Fourty",
        50: "Fifty",
        60: "Sixty",
        70: "Seventy",
        80: "Eighty",
        90: "Ninety",
    }
    es = {
        10: "Ten",
        11: "Eleven",
        12: "Twelve",
        13: "Thirteen",
        14: "Fourteen",
        15: "Fifteen",
        16: "Sixteen",
        17: "Seventeen",
        18: "Eighteen",
        19: "Nineteen",
    }

    res = []

    if part >= 100:
        res.append(a_[part // 100])
        res.append(" " + "Hundred" + " ")
        part = part % 100

    if 10 <= part < 19:
        res.append(es[part])

    else:
        if part >= 20:
            res.append(ties[(part // 10) * 10] + " ")
            part = part % 10
        if part >= 1:
            res.append(a_[part])

    return "".join(res)


def numToEnglish(num):
    if num == 0:
        return "Zero"

    units = ["", "Thousands", "Million", "Billion"]
    tmp = num
    cl = []
    i = 0
    while tmp:
        part = tmp % 1000
        if part != 0:
            part_words = process(part)
            if units[i]:
                cl.append(part_words + " " + units[i])
            else:
                cl.append(part_words)
        tmp //= 1000
        i += 1

    return " ".join(reversed(cl))
    # now we  will gonna  map the thing  called  millions  , some thing  like  that


if __name__ == "__main__":
    num = int(input("Enter the number : "))

    print(numToEnglish(num))
