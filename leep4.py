# suppose  we have this matrix  what you are seeing is row-wise and column-wise sorted matrix


# [
#     [1, 2,  5,   7],
#     [2, 6,  8,  11],
#     [3, 14, 16, 18]
# ]


#  we will gonna search in  stair case manner , we can  also go with naive o(n^2) but that is for beginners
#  this matrix have the proerty  which is not  strictly sorted where you see every  first element of row is greater than
#  last element of previous row last element which is not
#
#
#
#  Steps :
#  we will gonna start with lower bound as the lower = row[0] and  upper bound as the upper = max column
#  Then we will goo and check if the current element in matrix is equal to the target then wee will gonna return location of it
#  else , we will gonna check for that  if  the current  element is greater than given element than the all column will also  be greater than target we will move column --
#  else  we gonna move r++ if  the current element is less than the target then  row will contain all element less than that  r++


def searchMatrix(arr: list[list[int]], target: int) -> list[int, int]:
    rows = len(arr)
    cols = len(arr[0])

    row = 0
    col = (
        cols - 1
        # if  we dont have the square matrix then we will gonna use this , else you can go with the len(arr)-1
    )

    while row < rows and col > 0:
        if arr[row][col] == target:
            return [row, col]

        if arr[row][col] > target:
            col -= 1

        else:
            row += 1

    return [-1, -1]


mar = [[1, 2, 5, 7], [2, 6, 8, 11], [3, 14, 16, 18]]


mar1 = [[1, 2, 5], [7, 11, 15], [19, 21, 23]]


print(searchMatrix(mar, 14))


def searchMatrix1(matrix: list[list[int]], target: int) -> list[int, int]:
    # rows = len(matrix)
    cols = len(matrix[0])

    top = 0
    bottom = cols - 1
    while top <= bottom:
        mid = (top + bottom) // 2

        if matrix[mid][0] <= target <= matrix[mid][-1]:
            top = mid
            break
        if matrix[mid][0] > target:
            bottom = mid - 1
        else:
            top = mid + 1

    # row = (top+bottom)//2

    left = 0
    right = cols - 1

    while left <= right:
        mid = (left + right) // 2

        if matrix[top][mid] == target:
            return [top, mid]

        if matrix[top][mid] > target:
            right = mid - 1

        else:
            left = mid + 1

    return [-1, -1]


print(searchMatrix1(mar1, 19))
