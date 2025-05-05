# here we are exploring something which can be done to optimize the thing


# we have n X n board, which will be used
# explore all paths , means  visit  each and every thing and return the
# number of paths


def dfs(n, grid, r, c, visited):
    if visited == n * n and r == n - 1 and c == n - 1:
        nu_vs = sum(sum(row) for row in grid)
        if nu_vs == 1:
            return 0
        return 1

    count = 0
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nr, nc = dr + r, dc + c
        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
            grid[nr][nc] = 0
            count += dfs(n, grid, nr, nc, visited + 1)
            grid[nr][nc] = 1

    return count


if __name__ == "__main__":
    n = int(input())
    gridd = [[1] * n for i in range(n)]

    if n > 7:
        gridd[1][0] = 0
        c = dfs(n, gridd, 1, 0, 1)
        print(c * 2)

    else:
        c = dfs(n, gridd, 0, 0, 0)
        print(c)


# i think  for n == 7 , there will be problem  of getting the thing more bad, like connected
