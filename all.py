# So we get selection sort first
#


def smallest(arr):
    arr_ind = 0
    arr_ = arr[0]

    for i in range(len(arr)):
        if arr[i] < arr_:
            arr_ = arr[i]
            arr_ind = i

    return arr_ind


def selection(arr):
    arr_l = arr
    new_arr = []

    for _ in range(len(arr_l)):
        sma = smallest(arr_l)
        new_arr.append(arr_l.pop(sma))

    return new_arr


print(selection([8, 2, 31, 6, 81]))


# We  got the best way to use the  selection sort
def smallest_1(arr, start):
    arr_ind = start
    arr_ = arr[start]

    for i in range(start, len(arr)):
        if arr[i] < arr_:
            arr_ = arr[i]
            arr_ind = i

    return arr_ind


def selection_1(arr):

    for i in range(len(arr)):
        s = smallest_1(arr, i)
        temp = arr[i]
        arr[i] = arr[s]
        arr[s] = temp

    return arr


print(selection_1([7, 5, 2, 1, 8, 64]))


# one of the best  way to use the  quick sort using the  recursion
def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr if x < pivot]
        greater = [x for x in arr if x > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)


print(quick_sort([7, 5, 2, 1, 8, 64]))


# One thing  we  must  use  it in

def merge(arr, low, mid, high):

    n1 = mid-low+1
    n2 = high - mid

    l = [None] * n1
    r = [None] * n2

    for i in range(n1):
        l[i] = arr[low + i]

    for j in range(n2):
        r[j] = arr[mid + 1 + j]

    i = 0
    j = 0
    k = low
    while i < n1 and j < n2:
        if l[i] < r[j]:
            arr[k] = l[i]
            i += 1

        else:
            arr[k] = r[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = l[i]
        i += 1
        k += 1

    # Copy the remaining elements of r[], if there are any
    while j < n2:
        arr[k] = r[j]
        j += 1
        k += 1


def merge_sort(arr, low, high):
    if low >= high:
        return arr[low]

    mid = (low + high)//2

    merge_sort(arr, low, mid)
    merge_sort(arr, mid+1, high)
    merge(arr, low, mid, high)


if __name__ == "__main__":
    arr = [7, 8, 9, 5, 3, 2]
    merge_sort(arr, 0, len(arr) - 1)
    print(arr)


class Node:
    def __init__(self, data):
        self.next_reference = None
        self.data = data


class LinkedList:
    def __init__(self):
        self.Head = None

    def insertAtBeginning(self, value):
        l = Node(value)
        l.next_reference = self.Head
        self.Head = l

    def delete(self, key):
        temp = self.Head
        prev = None
        if (temp == self.Head and temp.data == key):
            self.Head = temp.next_reference
            return
        while (temp is not None and temp.data != key):
            prev = temp
            temp = temp.next_reference

        if (temp == None):
            return

        prev.next_reference = temp.next_reference

    def printList(self):
        temp = self.Head

        while (temp != None):
            print(temp.data, "->")
            temp = temp.next_reference

        print("NULL")
