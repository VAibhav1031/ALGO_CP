def maxOdd(arr):
    # take all positive integers to get the maximum sum,
    # if the sum is odd then return the sum but if the sum is even then find the smallest odd that can be subtracted.
    su_p = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            su_p += arr[i]
            # print(su_p)

    if su_p % 2 != 0:
        return su_p

    elif su_p % 2 == 0:
        smallest_odd = float("inf")
        for i in range(len(arr)):
            if arr[i] % 2 != 0 and abs(arr[i]) < smallest_odd:
                smallest_odd = abs(arr[i])

        if smallest_odd == float("inf"):
            smallest_odd = 1

        print(smallest_odd)
        return su_p - smallest_odd

    else:
        return -1


if __name__ == "__main__":
    n = list(map(int, input().split()))
    print(maxOdd(n))
