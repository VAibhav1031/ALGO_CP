## $$

# WE are building the  selection
#
#


def swap(A, g, h):
    tmp = A[g]
    A[g] = A[h]
    A[h] = tmp


def selection(A):
    for i in range(len(A)):
        n = A[i]
        j_ = 0
        for j in range(i, len(A)):
            if A[j] < n:
                n = A[j]
                j_ = j

            elif A[j] == n:
                j_ = j

        print(j_)
        swap(A, i, j_)


if __name__ == "__main__":
    n = list(map(int, input().split()))
    # swap(n, 1, 3)
    selection(n)
    print(n)
