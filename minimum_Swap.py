# 
# we want to know like how much swap it need to get the  sorted 


#  

class Solution:
    
    #Function to find the minimum number of swaps required to sort the array.
	def minSwaps(self, arr):
		#Code here
		
        # The  minimum swap needed   okay 
        temp = sorted(arr)
        
        pos = {}
        
        for i in range(len(arr)):
            pos[arr[i]] = i
            
            
        swaps = 0
        for i in range(len(arr)):
            if temp[i]!=arr[i]:
                ind = pos[temp[i]]  # we are getting the index of the  element  to which we are gonna swap the valye
                arr[i],arr[ind] = arr[ind],arr[i]
                
                
                pos[arr[i]] = i 
                pos[arr[ind]] = ind 

                swaps += 1 
                
        return swaps

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.minSwaps(arr)
        print(res)
        t -= 1