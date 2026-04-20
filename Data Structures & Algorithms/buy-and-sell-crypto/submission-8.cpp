class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int l = 0, r = numeric_limits<int>::min();

        for (int price : prices) {
            l = max(l, r + price);
            r = max(r, -price);
        }

        return l;
    }
};