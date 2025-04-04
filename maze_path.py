def allpath(path:str, arr, row:int, col:int, mat:list[int], step:int):

    if row == len(arr) - 1 and col == len(arr[0]) - 1:
        arr[row][col] = False
        mat[row][col] = step

        print()
        print(path)
        for i in mat:
            print(i)

        return

    if not arr[row][col]:
        return

    arr[row][col] = False
    mat[row][col] = step
    if row < len(arr) - 1:
        allpath(path + "D", arr, row + 1, col, mat, step + 1)

    if col < len(arr[0]) - 1:
        allpath(path + "R", arr, row, col + 1, mat, step + 1)

    if col > 0:
        allpath(path + "L", arr, row, col - 1, mat, step + 1)

    if row > 0:
        allpath(path + "U", arr, row - 1, col, mat, step + 1)

    arr[row][col] = True

    mat[row][col] = 0


pl = [
    [True, True, True],
    [True, True, True],
    [True, True, True]

]
mat = [[0, 0, 0] for _ in range(3)]
allpath('', pl, 0, 0, mat, 0)
