class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        dirs = ((1, 0), (0, 1), (-1, 0), (0, -1))
        visit = set()
        q = deque()
        dist = 1

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visit.add((r, c))

        while q:
            q_len = len(q)

            for _ in range(q_len):
                r, c = q.popleft()

                for dr, dc in dirs:
                    row, col = r + dr, c + dc
                    
                    if row in range(m) and col in range(n) and (row, col) not in visit and grid[row][col] != -1:
                        grid[row][col] = dist
                        q.append((row, col))
                        visit.add((row, col))

            dist += 1