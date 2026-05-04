dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
INF = 2147483647

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        q = deque((r, c) for r in range(m) for c in range(n) if not grid[r][c])
        dist = 1

        while q:
            for _ in repeat(None, len(q)):
                r, c = q.popleft()

                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == INF:
                        grid[nr][nc] = dist
                        q.append((nr, nc))

            dist += 1