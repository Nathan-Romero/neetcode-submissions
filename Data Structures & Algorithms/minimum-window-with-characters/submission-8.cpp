class Solution {
public:
    string minWindow(string s, string t) {
        unordered_map<char, int> s_count, t_count;

        for (char c : t) {
            t_count[c]++;
        }

        int l = 0;
        int have = 0, need = t_count.size();
        int start = -1;
        int res_len = INT_MAX;

        for (int r = 0; r < s.length(); r++) {
            s_count[s[r]]++;

            if (t_count.contains(s[r]) && s_count[s[r]] == t_count[s[r]]) {
                have++;
            }

            while (have == need) {
                if (r - l + 1 < res_len) {
                    res_len = r - l + 1;
                    start = l;
                }

                s_count[s[l]]--;

                if (t_count.contains(s[l]) && s_count[s[l]] < t_count[s[l]]) {
                    have--;
                }

                l++;
            }
        }

        return res_len == INT_MAX ? "" : s.substr(start, res_len);
    }
};