from typing import List


def Quick_sort(Arr: List):
    if len(Arr) <= 1:
        return Arr
    p = Arr[0]
    l1 = [i for i in Arr if i < p]
    l2 = [j for j in Arr if j > p]
    return Quick_sort(l1) + [p] + Quick_sort(l2)


if __name__ == "__main__":
    n = list(map(int, input().split()))
    print(Quick_sort(n))
