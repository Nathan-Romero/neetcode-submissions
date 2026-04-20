class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        dirs = ((1, 0), (0, 1), (-1, 0), (0, -1))
        visit = set()
        q = deque()
        dist = 1

        for r in range(m):
            for c in range(n):
                if not grid[r][c]:
                    q.append((r, c))
                    visit.add((r, c))

        while q:
            q_len = len(q)

            for _ in range(q_len):
                r, c = q.popleft()

                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visit and grid[nr][nc] != -1:
                        grid[nr][nc] = dist
                        q.append((nr, nc))
                        visit.add((nr, nc))

            dist += 1