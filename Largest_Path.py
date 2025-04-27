# Longest Possible Route in a Matrix with Hurdles
# Difficulty: MediumAccuracy: 50.0%Submissions: 15K+Points: 4Average Time: 15m
#
# Given an N x M matrix, with a few hurdles(denoted by 0) arbitrarily placed, calculate the length of the longest possible route possible from source(xs,ys) to a destination(xd,yd) within the matrix. We are allowed to move to only adjacent cells which are not hurdles. The route cannot contain any diagonal moves and a location once visited in a particular path cannot be visited again.If it is impossible to reach the destination from the source return -1.
#
#
#
# Example 1:
#
# Input:
# {xs,ys} = {0,0}
# {xd,yd} = {1,7}
# matrix = 1 1 1 1 1 1 1 1 1 1
#          1 1 0 1 1 0 1 1 0 1
#          1 1 1 1 1 1 1 1 1 1
# Output: 24
# Explanation:
#


class Solution:
    def longestPath(
        self, mat: list[list[int]], n: int, m: int, xs: int, ys: int, xd: int, yd: int
    ) -> int:
        # code here
        # we have  to code  this  thing like  similar to the rat in a maze problem where we have to do thing
        # but here we have said no diagonal  ,  so  we can  go in  adjacent  way  means  left right , up and down

        # now  it  is  something  here we have given is the  starting point
        # and the end point  where we have to go like  that  ,
        # LArgest possble  route means  a route with max  distance,  value  you can say

        dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def dfs(row, col, xd, yd, n, m, mat):
            """
            hey there
            """

            if (row, col) == (xd, yd):
                return 0

            if not (0 <= row < n and 0 <= col < m):
                return -(10**9)

            if mat[row][col] == 0:
                return -(10**9)

            current = mat[row][col]
            max_ = -(10**9)
            mat[row][col] = 0

            for dr, dc in dir:
                max_ = max(max_, dfs(row + dr, col + dc, xd, yd, n, m, mat))

            mat[row][col] = current

            # return current + max_
            return 1 + max_

        if mat[xs][ys] == 0 or mat[xd][yd] == 0:
            return -1

        lar_dist = dfs(xs, ys, xd, yd, n, m, mat)

        if lar_dist < 0:
            return -1

        return lar_dist
