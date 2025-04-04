# WE  are goonnaa  do  the merge  sort
#


# def merge(A, B, m, n):
#     i = 0
#     j = 0
#     k = 0
#
#     c = [None]*(m+n)
#     while i < m and j < n:
#         if A[i] < B[j]:
#             c[k] = A[i]
#             k += 1
#             i += 1
#
#         else:
#             c[k] = B[j]
#             k += 1
#             j += 1
#
#     if i < m:
#         for i in range(i, m):
#             c[k] = A[i]
#             k += 1
#
#
#     elif j < n:
#         for j in range(j, n):
#             c[k] = B[j]
#             k += 1
#
#     return c
#
#
# if __name__ == "__main__":
#     A = list(map(int, input().split()))
#     B = list(map(int, input().split()))
#     m = len(A)
#     n = len(B)
#     print(merge(A, B, m, n))
#
#


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


if __name__ == "__main__":
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    m = len(A)
    n = len(B)
    print(merge(A, B, m, n))
