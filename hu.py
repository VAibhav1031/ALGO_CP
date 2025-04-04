def hanoi(n, start, end):
    if n == 1:
        print(start, "->", end)

    else:
        other = 6 - (start + end)
        hanoi(n - 1, start, other)
        print(start, "->", end)
        hanoi(n - 1, other, end)


if __name__ == "__main__":
    n = int(input("Enter the Disks: "))
    s = int(input("Enter the start rod/peg : "))
    e = int(input("Enter the end rod/peg: "))

    hanoi(n, s, e)
