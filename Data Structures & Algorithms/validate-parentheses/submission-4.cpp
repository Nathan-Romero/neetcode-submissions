class Solution {
    unordered_map<char, char> pars{{')', '('}, {'}', '{'}, {']', '['}};

public:
    bool isValid(string s) {
        stack<char> stk;

        for (char c : s) {
            if (pars.contains(c)) {
                if (!stk.empty() && stk.top() == pars[c]) {
                    stk.pop();
                } else {
                    return false;
                }
            } else {
                stk.push(c);
            }
        }

        return stk.empty();
    }
};