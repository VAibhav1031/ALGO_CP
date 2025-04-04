# we are  gonna  make  the  merge  sort  here


def merge(A, B, m, n):
    i = 0
    j = 0
    k = 0

    c = []
    while i < m and j < n:
        if A[i] < B[j]:
            c.append(A[i])
            k += 1
            i += 1

        else:
            c.append(B[j])
            k += 1
            j += 1

    if i < m:
        c.extend(A[i:m])

    elif j < n:
        c.extend(B[j:n])

    return c


def Merge_sort(A, l_, h):
    if l_ == h:
        return [A[l_]]

    mid = (l_ + h) // 2
    left = Merge_sort(A, l_, mid)
    right = Merge_sort(A, mid + 1, h)

    return merge(left, right, len(left), len(right))


if __name__ == "__main__":
    n = list(map(int, input().split()))
    l_ = Merge_sort(n, 0, len(n) - 1)
    print(l_)
