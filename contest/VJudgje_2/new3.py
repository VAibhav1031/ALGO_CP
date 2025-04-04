t = int(input())


def isEqual(s):

    s.sort(reverse=True)
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            new_val = s[i] * 2

            s.pop(i)
            s.pop(i)
            s.append(new_val)
            return [new_val], s


    return [], s


def isTwo_zero_four_eight(li, s):

    s.append(sum(li))
    if 2048 in s:
        return True

    while True:

        li, s = isEqual(s)
        if not li:
            break

        if 2048 in s:
            return True

    return False


while t:
    t -= 1
    n = int(input())
    s = list(map(int, input().split()))

    if 2048 in s:
        print("YES")
    else:
        if isTwo_zero_four_eight([], s):
            print("YES")
        else:
            print("NO")
