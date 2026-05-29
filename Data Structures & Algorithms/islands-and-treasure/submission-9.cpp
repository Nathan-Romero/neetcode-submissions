class Solution {
    array<pair<int, int>, 4> dirs {{{0, 1}, {0, -1}, {1, 0}, {-1, 0}}};

public:
    void islandsAndTreasure(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        int dist = 1;
        queue<pair<int, int>> q;

        for (int r = 0; r < m; ++r) {
            for (int c = 0; c < n; ++c) {
                if (!grid[r][c]) {
                    q.push({r, c});
                }
            }
        }

        while (!q.empty()) {
            int k = q.size();
            for (int i = 0; i < k; ++i) {
                const auto [r, c] = q.front();
                q.pop();

                for (const auto& [dr, dc] : dirs) {
                    int nr = r + dr, nc = c + dc;
                    if (nr != -1 && nr != m && nc != -1 && nc != n && grid[nr][nc] == numeric_limits<int>::max()) {
                        grid[nr][nc] = dist;
                        q.push({nr, nc});
                    }
                }
            }
            ++dist;
        }
    }
};
