class Solution {
    string s;
    vector<string> part;
    vector<vector<string>> res;

    void dfs(int i) {
        if (i == s.length()) {
            res.push_back(part);
            return;
        }

        for (int j = i; j < s.size(); ++j) {
            if (is_pali(i, j)) {
                part.push_back(s.substr(i, j - i + 1));
                dfs(j + 1);
                part.pop_back();
            }
        }
    }

    bool is_pali(int l, int r) {
        while (l < r) {
            if (s[l] != s[r]) {
                return false;
            }
            ++l, --r;
        }
        return true;
    }

public:
    vector<vector<string>> partition(string s) {
        this->s = s;
        dfs(0);
        return res;
    }
};
