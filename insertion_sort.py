# i am goonna  do the  insertion, selection , bubble sort 
# these are important one also 

#Insertion sort ::
# -->Insertion sort is a simple sorting algorithm that works by iteratively inserting each element of an unsorted list into its correct position in a sorted portion of the list. It is like sorting playing cards in your hands. You split the cards into two groups: the sorted cards and the unsorted cards. Then, you pick a card from the unsorted group and put it in the right place in the sorted group.

#     We start with second element of the array as first element in the array is assumed to be sorted.
#     Compare second element with the first element and check if the second element is smaller then swap them.
#     Move to the third element and compare it with the first two elements and put at its correct position
#     Repeat until the entire array is sorted.


def insertionSort(nums: list[int])->list[int]:
    for i in range(1, len(nums)):
        cur = i 
        while cur and nums[cur] < nums[cur-1]:
            if nums[cur]<nums[cur-1]:
                nums[cur],nums[cur-1] = nums[cur-1],nums[cur]
            cur-=1 
 

n = [13, 7, 1, 2 ,11]
insertionSort(n)
print(n)
#  here the time complexity will be  the 
# o(n) -->  best if  we got already a sorted array 
# o(n^2)--> average 
# o(n^2) -->  worst  when array is reverse sorted


# there is one more  way to do is  like 
# in this  we are gonna  make  greater element to the right if  there are else nothing will gonna happen

def insertionSort1(nums: list[int])-> list[int]:
    for i in range(1, len(nums)):
        key = nums[i]
        j = i-1

        while j>=0 and nums[j]>key:
            nums[j+1] = nums[j]
            j-=1
        nums[j+1] = key
   
# n = [13, 1, 5, 2 ,11,8]
n = [2,0,2,1,1,0]
insertionSort1(n)
print(n)



#REcursive Approach :--
# now  we have  to create the  REcursive Approach of thtis 


def insertionSortRecursive(arr, n=None):
    # Initialize n to the length of the array on first call
    if n is None:
        n = len(arr)
    
    # Base case: if array is sorted (n <= 1)
    if n <= 1:
        return
    
    # Sort first n-1 elements recursively
    insertionSortRecursive(arr, n-1)
    
    # Insert the nth element into the sorted array [0...n-1]
    key = arr[n-1]
    j = n-2
    
    # Move elements greater than key one position ahead
    while j >= 0 and arr[j] > key:
        arr[j+1] = arr[j]
        j -= 1
    
    # Place key at the correct position
    arr[j+1] = key


    
ni = [9,6,5,2,1,4]
insertionSortRecursive(ni)
print(ni)







 



















