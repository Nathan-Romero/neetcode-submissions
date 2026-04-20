from functools import cache

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dirs = ((1, 0), (0, 1), (-1, 0), (0, -1))
        res = 0

        @cache
        def dfs(r, c, prev):
            if min(r, c) < 0 or r >= m or c >= n or matrix[r][c] <= prev:
                return 0

            res = 1
            for dr, dc in dirs:
                res = max(res, 1 + dfs(r + dr, c + dc, matrix[r][c]))

            return res

        for r in range(m):
            for c in range(n):
                res = max(res, dfs(r, c, float('-inf')))

        return res