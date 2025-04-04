# we are gonna  do  the  sorting  thing here


# 1. Quick Sort :


def swap(A, g, h):
    t = A[g]
    A[g] = A[h]
    A[h] = t


def partition(A, l_, h):
    p = A[l_]
    i = l_
    j = h

    while True:
        while i <= h and A[i] <= p:
            i += 1

        while j >= l_ and A[j] > p:
            j -= 1

        if i >= j:
            break
        swap(A, i, j)

    mid = (i + j) // 2
    swap(A, l_, mid)
    return j


def quick_sort(A, L, H):
    if L < H:
        j = partition(A, L, H)
        quick_sort(A, L, j - 1)
        quick_sort(A, (j + 1), H)


if __name__ == "__main__":
    n = list(map(int, input().split()))
    L = 0
    H = len(n) - 1
    quick_sort(n, L, H)
    print(n)
