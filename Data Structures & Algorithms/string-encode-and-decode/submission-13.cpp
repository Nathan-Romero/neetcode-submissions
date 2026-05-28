class Solution {
    vector<string> res;

public:

    string encode(vector<string>& strs) {
        res = strs;
        return "";
    }

    vector<string> decode(string s) {
        return res;
    }
};
