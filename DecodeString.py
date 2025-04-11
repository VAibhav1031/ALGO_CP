def decodeString(s: str):
    """
    we  will use the stack  to  do  the things
    """

    # make a append to the stack  and  then  whenever we encounter the "]"
    # close thing we must pop and  print

    # 3[a]2[bc]
    l = []
    while s:
        if s[0] == "]":
            a_char = []
            digits = ""
            while not l[-1].isdigit():
                if l[-1] == "[":
                    l.pop()
                    continue
                a_char.append(l.pop())

            while l and l[-1].isdigit():
                digits += l.pop()

            new_s = "".join(reversed(a_char)) * int(digits[::-1])
            l.append(new_s)
        else:
            l.append(s[0])
        s = s[1:]

    return "".join(l)


print(decodeString("3[z]2[2[y]pq4[2[jk]e1[f]]]ef"))
