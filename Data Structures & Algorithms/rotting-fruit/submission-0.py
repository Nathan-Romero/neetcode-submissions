class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()

        def bfs(r, c):
            if (min(r, c) < 0 or r >= ROWS or c >= COLS or
                grid[r][c] == 0
            ):
                return

            if grid[r][c] == 1:
                q.append([r, c])
                grid[r][c] = 2

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append([r, c])

        time = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                bfs(r + 1, c)
                bfs(r - 1, c)
                bfs(r, c + 1)
                bfs(r, c - 1)

            if not q:
                break
            time += 1
        
        for r in grid:
            if 1 in r:
                return -1
        
        return time