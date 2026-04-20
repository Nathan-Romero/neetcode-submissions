class Solution {
public:
    int findMin(vector<int>& nums) {
        return *ranges::min_element(nums);
    }
};