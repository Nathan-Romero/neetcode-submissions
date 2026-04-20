class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int* prev = &prices[0];
        int res = 0;

        for (int& price : prices) {
            if (*prev < price) {
                res = max(res, price - *prev);
            } else {
                prev = &price;
            }
        }
        return res;
    }
};
