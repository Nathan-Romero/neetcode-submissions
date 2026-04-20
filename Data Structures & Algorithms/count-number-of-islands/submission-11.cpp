class Solution {
    int dirs[4][2] = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
public:
    int numIslands(vector<vector<char>>& grid) {
        int m = grid.size(), n = grid[0].size();
        int res = 0;

        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (grid[r][c] == '1') {
                    dfs(r, c, grid);
                    res++;
                }
            }
        }

        return res;
    }

private:
    void dfs(int r, int c, vector<vector<char>>& grid) {
        if (r < 0 || c < 0 || r >= grid.size() || c >= grid[0].size() || grid[r][c] == '0') {
            return;
        }

        grid[r][c] = '0';

        for (const auto& [dr, dc] : dirs) {
            dfs(r + dr, c + dc, grid);
        }
    }
};
