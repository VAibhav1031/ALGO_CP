### Bucket  sort
import math


def insertionSort(arr):
    for i in range(1, len(arr)):
        t = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > t:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = t


def bucketSort(arr):
    n = len(arr)
    m = max(max(arr), n)

    nob = 10

    divider = math.ceil((m + 1) / nob)
    b = [[] for _ in range(10)]

    for i in range(n):
        j = arr[i] // divider
        b[j].append(arr[i])  #  problem - idk

    for i in range(nob):
        insertionSort(b[i])

    b_final = [i for k in b for i in k]

    return b_final


if __name__ == "__main__":
    n = list(map(int, input().split()))
    print()
    print()
    print(bucketSort(n))
