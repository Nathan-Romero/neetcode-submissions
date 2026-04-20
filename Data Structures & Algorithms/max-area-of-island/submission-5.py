class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        seen = set()
        res = 0

        def dfs(r, c):
            if min(r, c) < 0 or r >= m or c >= n or grid[r][c] == 0 or (r, c) in seen:
                return 0

            seen.add((r, c))

            return 1 + (
                dfs(r + 1, c) +
                dfs(r, c + 1) +
                dfs(r - 1, c) +
                dfs(r, c - 1)
            )

        for r in range(m):
            for c in range(n):
                res = max(res, dfs(r, c))

        return res