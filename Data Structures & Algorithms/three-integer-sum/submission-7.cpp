#include <ranges>

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> res;

        for (const auto& [i, n] : views::enumerate(nums)) {
            if (i && n == nums[i - 1]) continue;
            int l = i + 1, r = nums.size() - 1;

            while (l < r) {
                int cur_sum = n + nums[l] + nums[r];

                if (cur_sum < 0) {
                    l++;
                } else if (cur_sum > 0) {
                    r--;
                } else {
                    res.push_back({n, nums[l], nums[r]});
                    l++; r--;

                    while (l < r && nums[l] == nums[l - 1]) {
                        l++;
                    }
                    while (l < r && nums[r] == nums[r + 1]) {
                        r--;
                    }
                }
            }
        }

        return res;
    }
};