def countingSort(arr):
    k = max(arr)
    count = [0] * (k + 1)
    og = [0] * len(arr)

    for i in range(len(arr)):
        count[arr[i]] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for i in range(len(arr) - 1, -1, -1):
        count[arr[i]] -= 1
        og[count[arr[i]]] = arr[i]

    return og


if __name__ == "__main__":
    n = list(map(int, input().split()))
    print(countingSort(n))
