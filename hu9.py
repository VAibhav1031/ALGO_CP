def linearProbing(keys):
    d = [0] * len(keys)
    for i in range(len(keys)):
        index = keys[i] % len(keys)
        if d[index] != 0:
            for j in range(len(keys)):
                ind = (index + j) % len(keys)
                if d[ind] == 0:
                    index = ind
                    break
        d[index] = keys[i]

    return d


if __name__ == "__main__":
    n = list(map(int, input().split()))
    print(linearProbing(n))
