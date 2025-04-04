##

# bubble sort


def bubble(A):
    for i in range(len(A) - 1):
        for j in range(len(A) - i - 1):
            if A[j] > A[j + 1]:
                temp = A[j]
                A[j] = A[j + 1]
                A[j + 1] = temp


if __name__ == "__main__":
    n = list(map(int, input().split()))
    bubble(n)
    print(n)
