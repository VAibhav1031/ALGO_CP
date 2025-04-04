# def canCut(rope, k, rope_length):
#     ro = 1 
#     current_sum = 0 
#
#     for l in rope:
#         if l > rope_length:
#             return False 
#
#         if l + current_sum > rope_length:
#             ro += 1 
#             current_sum = l 
#
#             if ro > k:
#                 return False 
#         else:
#             current_sum += l
#
#     return True
#
#
# def minimumLenOfRope(arr, k):
#     lo , hi = max(arr), sum(arr)
#     reuslt = hi 
#
#     while lo <=  hi :
#         mid = (lo + hi)//2
#         if canCut(arr,k, mid):
#             reuslt = mid
#             hi = mid-1 
#
#         else:
#             lo = mid + 1 
#
#     return reuslt 


def isValidTime(fuel, h, mid):
    ho = 0
    for f in fuel:
        ho += ceil(p/mid)

    return ho <= h

def minimumTimeTofill(arr, h):
    lo, hi = max(arr), sum(arr) 
    reuslt = 0
    while lo < hi:
        mid = (lo+hi)//2 
        if isValidTime(arr, h):
            reuslt = mid
            hi = mid-1 
        else:
            lo = mid+1 

    return reuslt

if __name__ == "__main__":
    n = list(map(int, input().split()))

    K_ = int(input("Enter K :  "))
    print(minimumTimeTofill(n, K_))
