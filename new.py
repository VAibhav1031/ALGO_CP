def binary(arr, item, low, high):
    if low > high:
        return "Item not found"

    mid = (low + high)//2
    guess = arr[mid]

    if guess == item:
        return f"The Item {guess}  is  at {mid}"

    elif guess > item:
        return binary(arr, item, low, mid-1)
    else:
        return binary(arr, item, mid+1, high)


def main(arr, item):
    low = 0
    high = len(arr)-1
    return binary(arr, item, low, high)


if __name__ == "__main__":
    result = main([1, 5, 6, 8, 9], 1)
    print(result)
