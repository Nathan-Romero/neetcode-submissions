class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dirs = ((1, 0), (0, 1), (-1, 0), (0, -1))
        res = fresh = 0
        q = deque()

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    fresh += 1

                elif grid[r][c] == 2:
                    q.append((r, c))

        while q and fresh:
            q_len = len(q)

            for _ in range(q_len):
                r, c = q.popleft()

                for dr, dc in dirs:
                    row, col = r + dr, c + dc

                    if row in range(m) and col in range(n) and grid[row][col] == 1:
                        grid[row][col] = 2
                        q.append((row, col))
                        fresh -= 1

            res += 1

        return res if not fresh else -1