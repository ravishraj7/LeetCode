class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])

       
        prev = [set() for _ in range(n)]
        for i in range(m):
            cur = [set() for _ in range(n)]
            for j in range(n):
                v = grid[i][j]
                if i == 0 and j == 0:
                    cur[j] = {v}
                    continue
                s = set()
                if i > 0:
                    s |= prev[j]
                if j > 0:
                    s |= cur[j - 1]
                cur[j] = {x ^ v for x in s}
            prev = cur

        return min(prev[n - 1])