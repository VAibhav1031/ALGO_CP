def mountainPeak(nums: list[int]):
    low = 0
    high = len(nums)-1 

    while low<=high:
        mid = (low+high)//2 
        if nums[mid]>nums[mid+1]:
            high = mid-1
        else:
            low = mid+1 
    return low

print(mountainPeak([1,2,3,5,6,4,3,2,1]))
