def findFirstNonRepeating(s: str):
    # if we have  to print only the  first non repeating only
    from collections import Counter

    s_ = Counter(s)

    for key, value in s_.items():
        if value == 1:
            return key


if __name__ == "__main__":
    st = input()
    print(findFirstNonRepeating(st))


# if  asked to print the second or third store the all k which have 1 serial wise(which will be happen ) and return according to need
