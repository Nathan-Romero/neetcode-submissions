class TrieNode {
public:
    unordered_map<char, TrieNode*> children;
    bool is_word;
    TrieNode() : is_word(false) {}

    void insert(const string& word) {
        TrieNode* node = this;

        for (char c : word) {
            if (!node->children.count(c)) {
                node->children[c] = new TrieNode();
            }
            node = node->children[c];
        }
        node->is_word = true;
    }
};

class Solution {
public:
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        this->board = board;
        TrieNode* root = new TrieNode();
        for (const auto& word : words) {
            root->insert(word);
        }
        m = board.size(), n = board[0].size();
        visited.assign(m, vector<bool>(n));

        for (int r = 0; r < m; ++r) {
            for (int c = 0; c < n; ++c) {
                dfs(r, c, root, "");
            }
        }
        return vector<string>(res.begin(), res.end());
    }

private:
    int m, n;
    unordered_set<string> res;
    vector<vector<bool>> visited;
    vector<vector<char>> board;

    void dfs(int r, int c, TrieNode* node, string word) {
        if (r == -1 || r == m || c == -1 || c == n || visited[r][c] || !node->children.count(board[r][c]))
            return;

        visited[r][c] = true;
        node = node->children[board[r][c]];
        word += board[r][c];
        if (node->is_word)
            res.insert(word);

        dfs(r + 1, c, node, word);
        dfs(r - 1, c, node, word);
        dfs(r, c + 1, node, word);
        dfs(r, c - 1, node, word);
        visited[r][c] = false;
    }
};
