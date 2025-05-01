# Consider a rat placed at position (0, 0) in an n x n square matrix mat[][].
# The rat's goal is to reach the destination at position (n-1, n-1).
# The rat can move in four possible directions: 'U'(up), 'D'(down), 'L' (left), 'R' (right).
#
# The matrix contains only two possible values:
#
#     0: A blocked cell through which the rat cannot travel.
#     1: A free cell that the rat can pass through.
#
# Your task is to find all possible paths the rat can take to reach the destination,
# starting from (0, 0) and ending at (n-1, n-1),
# under the condition that the rat cannot revisit any cell along the same path. Furthermore,
# the rat can only move to adjacent cells that are within the bounds of the matrix and not blocked.
# If no path exists, return an empty list.
#
# Note: Return the final result vector in lexicographically smallest order.
#
# Examples:
#
# Input: mat[][] = [[1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]]
# Output: ["DDRDRR", "DRDDRR"]
# Explanation: The rat can reach the destination at (3, 3) from (0, 0) by two paths - DRDDRR and DDRDRR,
# when printed in sorted order we get DDRDRR DRDDRR.


def ratMAze(maze, row, col, paths, proc):
    if row == len(maze) - 1 and col == len(maze[0]) - 1:
        paths.append(proc)
        return

    if (
        row < 0
        or col < 0
        or row >= len(maze)
        or col >= len(maze[0])
        or maze[row][col] == 0
    ):
        return

    maze[row][col] = 0
    ratMAze(maze, row + 1, col, paths, proc + "D")
    ratMAze(maze, row, col + 1, paths, proc + "R")
    ratMAze(maze, row - 1, col, paths, proc + "U")
    ratMAze(maze, row, col - 1, paths, proc + "L")
    maze[row][col] = 1


# dont get  confused with  the below  function why we are not using the backtracking point  here , the  reason here is we are only using the  Down and Right
# which  never  ever let us  to revisit  the visited  cell, and all things so  the  concept of  being  we dont have to  revisit the visited cell is  implicitly
# following, we dont have to do nothing .
#
# you can try  and think  Down and right will never make recursion loop
#
# unless until  we will use all four  which can make  us to revisit the visited cell and  calling same thing again and again


def ratMaze(maze, row, col, paths, proc):
    if row == len(maze) - 1 and col == len(maze[0]) - 1:
        paths.append(proc)
        return

    if (
        row < 0
        or col < 0
        or row >= len(maze)
        or col >= len(maze[0])
        or not maze[row][col]
    ):
        return

    ratMaze(maze, row + 1, col, paths, proc + "D")
    ratMaze(maze, row, col + 1, paths, proc + "R")


if __name__ == "__main__":
    maze = [[1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]]

    n = len(maze)
    paths = []
    ratMaze(maze, 0, 0, paths, "")
    print(paths)
