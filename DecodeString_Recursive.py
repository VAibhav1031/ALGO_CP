# we will add the thing called


def decodeString(s: str, index, result):
    if index >= len(s):
        return result, index

    if s[index] == "]":
        return result, index

    if s[index].isdigit():
        # gather whole digits
        #
        # can we use the loop to get the full
        num = 0
        while s[index].isdigit():
            num = num * 10 + int(s[index])
            index += 1

        if s[index] == "[":
            index += 1

        decode_string, index = decodeString(s, index, "")

        result += num * decode_string

        return decodeString(s, index + 1, result)

    # else we are gonna add the character to the result
    else:
        return decodeString(s, index + 1, result + s[index])


print(decodeString("3[a2[c]]", 0, "")[0])
print()
print(decodeString("100[leetcode]", 0, "")[0])

print(decodeString("3[z]2[2[y]pq4[2[jk]e1[f]]]ef", 0, "")[0])
