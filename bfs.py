# helllo guys  we are going to complete the bfs
# most of the variation i am going to learn

from collections import deque

from typing import List


class Solution:
    def countIslands(self, grid, row, col, visited):
        queue = deque()
        queue.append((row, col))

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        # visited = set()

        # we have to see where we have to count the things bro
        while len(queue):
            row, col = queue.popleft()
            # visited.add((row, col))
            for dr, dc in directions:
                nr, nc = dr + row, dc + col

                if (
                    0 <= nr < len(grid)
                    and 0 <= nc < len(grid[0])
                    and (nr, nc) not in visited
                    and grid[nr][nc] == "1"
                ):
                    queue.append((nr, nc))
                    visited.add((nr, nc))

    def numIslands(self, grid: List[List[str]]) -> int:
        # okay  lets  so

        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    count += 1
                    self.countIslands(grid, r, c, visited)
        return count
