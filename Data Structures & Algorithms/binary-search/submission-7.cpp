class Solution {
public:
    int search(vector<int>& nums, int target) {
        auto it = lower_bound(nums.begin(), nums.end(), target);
        int i = distance(nums.begin(), it);

        return i < nums.size() && nums[i] == target ? i : -1;
    }
};
