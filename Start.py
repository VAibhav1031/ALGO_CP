# This  is the basic
#

def binary_search(arr, item):
    low = 0
    high = len(arr)-1

    while low <= high:

        mid = (high + low)//2
        guess = arr[mid]

        if guess == item:
            return guess

        elif guess > item:
            high = mid - 1

        elif guess < item:
            low = mid + 1

        else:
            return None


print(binary_search([1, 5, 6, 8, 9], 9))


def binary_search1(arr, item, low, high):
    mid = (high + low)//2
    guess = arr[mid]
    if guess == item:
        return item

    else:
        if guess > item:
            binary_search1(arr, item, low, mid-1)

        else:
            binary_search1(arr, item, (mid+1), high)


print(binary_search1([1, 5, 6, 8, 9], 9, 0, 4))


def fin(n: int, mem) -> int:

    if n in mem.keys():
        return mem[n]

    else:

        if n <= 2:
            return 1
        else:
            mem[n] = fin(n-1, mem) + fin(n-2, mem)
            return mem[n]


mem = {}
print(fin(10, mem))


def smallest(arr):
    arr_inde = 0
    smalle = arr[0]
    if len(arr) <= 1:
        return arr
    for i in range(1, len(arr)):
        if arr[i] < smalle:
            arr_inde = i
            smalle = arr[i]
    return arr_inde


print(smallest([4, 28, 9, 5, 6, 3, 1, 11]))


def selection(arr):

    new_arr = []
    for _ in arr:
        sma = smallest(arr)
        new_arr.append(arr.pop(sma))

    return new_arr


print(selection([7, 2, 6, 7, 4, 1, 2, 6, 9]))


def quick_sort(arr):
    if len(arr) < 2:
        return arr

    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x < pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


print(quick_sort([8, 1, 3, 9, 4, 13]))
