class Solution {
    int m, n;
    vector<vector<char>> board;
    string word;

    bool dfs(int r, int c, int i) {
        if (i == word.size()) {
            return true;
        }
        if (r < 0 || c < 0 || r == m || c == n || board[r][c] != word[i] || board[r][c] == '#') {
            return false;
        }

        board[r][c] = '#';
        bool res = dfs(r + 1, c, i + 1) || dfs(r - 1, c, i + 1) || dfs(r, c + 1, i + 1) ||
                   dfs(r, c - 1, i + 1);
        board[r][c] = word[i];
        return res;
    }

   public:
    bool exist(vector<vector<char>>& board, string word) {
        m = board.size(), n = board[0].size();
        this->board = board;
        this->word = word;

        for (int r = 0; r < m; ++r) {
            for (int c = 0; c < n; ++c) {
                if (dfs(r, c, 0)) {
                    return true;
                }
            }
        }
        return false;
    }
};
