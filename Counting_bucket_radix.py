# Counting Sort:

# Easy-peasy 
def countingSort(nums :list[int]):
    # since  we have to make  the frequency counter first then we will gonna  do the  cumulative sum of that 
    
    s = [0]*(max(nums)+1)
    output = [0]*(len(nums))
    for n in nums:
        s[n]+=1
        
            
    # cumulative sum of it 
    
    for i in range(1, len(s)):
        s[i] += s[i-1]
    
    # now  we are going place the thing 
    
    for i in range(len(nums)-1,-1,-1):
        s[nums[i]] -= 1  # because we follow the 0 based indexing in the array 
        output[s[nums[i]]] = nums[i] 

    return output
print(countingSort([2, 3, 2, 1, 4, 2]))
        
        
        
def countingSortForRadix(nums: list[int], exp):
    n = len(nums)
    count = [0]*10
    output = [0] *n
    
    
    for u in nums:
        count[(u//exp)%10] += 1 
        
        
        
    for i in range(1, len(count)):
        count[i] += count[i-1]
        
        
    for i in range(n-1, -1, -1):
        count[(nums[i]//exp)%10]-=1 
        
        output[count[(nums[i]//exp)%10]] = nums[i]
        
    
    for i in range(n):
        nums[i] = output[i]
        

    
def radixSort(nums):
    max_val = max(nums)
    
    exp = 1
    while max_val//exp>0:
        countingSortForRadix(nums, exp)
        exp *= 10
        
        
# simple  is  the thing where // will be used to get remove the last element % to get the last 
# we start basically from exp = 1  because for getting the last element also then move 

        
n = [-2,-5,-1,]
radixSort(n)

print(n)

#  The radix sort is not designed to handle  to the negative numbers using the negative numbers will give wrong answer
# it may give  that negative will be behind the positive  which may give wrong output because of this  

#  we can separte the negative number from main  array and  sort the main  and sort the negative(by treating them as the positive)
# then combine them  by reversing negative (treated as positive) sorted array 

# or you can  do the one thing where we can use one thing take  one offset value which is  the absolute value of  the smallest element in the array( - one)
#  first we are gonna  add the  off set one  to all value sort them  ,  negative will become the 0 and  it will at first and then  after sorting we are gonna remove the off set one from the array 


if __name__ == "__main__":
    n = list(map(int, input().strip().split()))
    s = min(n)
    if s < 0 :
        for i in range(len(n)):
            n[i]+= abs(s)
            
            
        radixSort(n)
        
        for i in range(len(n)):
            n[i] -= abs(s)

    else:
        radixSort(n)
        

    