class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        inf = 2147483647
        dirs = (0, 1), (1, 0), (0, -1), (-1, 0)
        m, n = len(grid), len(grid[0])
        q = deque([(r, c) for r in range(m) for c in range(n) if not grid[r][c]])
        dist = 1

        while q:
            for _ in repeat(None, len(q)):
                r, c = q.popleft()
                for dr, dc in dirs:
                    if 0 <= (nr := r + dr) < m and 0 <= (nc := c + dc) < n and grid[nr][nc] == inf:
                        grid[nr][nc] = dist
                        q.append((nr, nc))
            dist += 1