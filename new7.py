#  we  are gonna  do some  insertion sort
#
#


# def insertion(A):
#     for i in range(1, len(A)):
#         temp = A[i]
#
#         for j in range(i - 1, -1, -1):
#             if A[j] > temp:
#                 A[i] = A[j]
#                 A[j] = temp
#                 i = i - 1
#
#             elif A[j] < temp:
#                 continue
#
#
# if __name__ == "__main__":
#     n = list(map(int, input().split()))
#     insertion(n)
#     print(n)
#


def insertion(A):
    for i in range(1, len(A)):
        temp = A[i]
        j = i - 1

        while j >= 0 and A[j] > temp:
            A[j + 1] = A[j]
            j -= 1

        A[j + 1] = temp


if __name__ == "__main__":
    n = list(map(int, input().split()))
    insertion(n)
    print(n)
