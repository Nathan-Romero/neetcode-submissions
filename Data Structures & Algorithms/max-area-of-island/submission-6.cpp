class Solution {
    int m, n;
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        m = grid.size(), n = grid[0].size();
        int res = 0;

        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (grid[r][c]) {
                    res = max(res, dfs(r, c, grid));
                }
            }
        }

        return res;
    }

private:
    int dfs(int r, int c, vector<vector<int>>& grid) {
        if (r < 0 || c < 0 || r >= m || c >= n || !grid[r][c]) {
            return 0;
        }

        grid[r][c] = 0;

        return 1 + dfs(r + 1, c, grid) + dfs(r, c + 1, grid) + dfs(r - 1, c, grid) + dfs(r, c - 1, grid);
    }
};
