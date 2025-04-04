# square  root  estimation :


def sqrtEstimation(x: int) -> int:
    lo = 0
    hi = x
    mid = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        if mid * mid == x:
            break
        if mid * mid <= x:
            lo = mid + 1

        else:
            hi = mid - 1

    return mid


# Thing is  to  use  the   some other  way where  we can get teh  accuracy near  to  the  answer  so  we  think
# to  use  the newton  raphson  method  which  is  very  good
#


def newtonRaphson(x: int):
    tolerance = 1e-2
    y = x / 2
    while abs(y * y - x) > tolerance:
        y = (y + (x / y)) / 2

    return y


if __name__ == "__main__":
    t = int(input())
    print(sqrtEstimation(t))
    print()
    print(newtonRaphson(t))
