# def searchMatrix(matrix: list[list[int]], target: int) -> bool:
#     # it is different from  other search because matrix is sorted differently 
#     # it is not sorted like  previous search in 2d matrix where we have given strictly 
#     # sorte matrix which require different way to check up on 

#     # this one is somple because each and evry row are sorted differently
    


#     rows = len(matrix)
#     cols = len(matrix[0])
    
#     row ,col = 0, rows-1
#     while row< rows and col>0:
#         if row==-1 and col ==-1:
#             return False
#         if matrix[row][col] == target:
#             return True  
#         if matrix[row][col]>target:  # if the current column element is greater than require than whole column is greater than the target and move the column  to -1  or less one 
#             col -= 1
#         else:

#             # if the current elemen in the row is having less than target than the whole row is having less than target then  move to new row 
#             row+=1


#     return False
    
    
# print(searchMatrix([[1,1]],2))


# now we have the  matrix which is  strictly sorted
# [
#     [1,   2,   5],
#     [7,  11,  15],
#     [19, 21,  23]
# ]


# in this if you see there is strictly sorted so  normal  
# we cant use the  way  of  using the normal row and columnwise because here you will see something different 
def searchMatrix1(matrix : list[list[int]], target: int)->list[int,int]:
    rows = len(matrix)
    cols = len(matrix[0])
    
    
    top = 0
    bottom = cols - 1
    while top<=bottom:
        mid = (top+bottom)//2 

        if matrix[mid][0]<target<matrix[mid][-1]:
            break
        if matrix[mid][0] >target:
            bottom = mid - 1 
        else:
            top = mid + 1
            
            
    row = (top+bottom)//2 
    
    left = 0
    right = cols-1
    
    while left<=right:
        mid = (left+right)//2 
        
        
        if matrix[row][mid] == target:
            return [row,mid]
            
            
        if matrix[row][mid]>target:
            right = mid-1 
            
        else:
            left = mid+1 
            
            
    return [-1,-1]
    
    
