#  we  are doing the  thing for  the   radix sort  using the help  of the  counting sort in subroutines
#
#  means   if  we have  3 digit  number then  we start  apply it on LSB and  then  move to  the  MSB  (RIGHT to LEFT)
#  This  will help in doing the radix sort  working  so radix  working  totally dependant  on the  counting sort
#
#


def countingSort_for_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for num in arr:
        index = (num // exp) % 10
        count[index] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for i in range(len(arr) - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    for i in range(len(arr)):
        arr[i] = output[i]


def radixSort(arr):
    max_val = max(arr)

    exp = 1

    while max_val // exp > 0:
        countingSort_for_radix(arr, exp)
        exp *= 10


if __name__ == "__main__":
    n = list(map(int, input().split()))

    radixSort(n)

    print(n)
