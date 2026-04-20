class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> res(n - k + 1);
        deque<int> q;
        int l = 0;

        for (int r = 0; r < n; r++) {
            while (!q.empty() && nums[q.back()] < nums[r]) {
                q.pop_back();
            }
            q.push_back(r);

            if (l > q.front()) {
                q.pop_front();
            }

            if (r + 1 >= k) {
                res[l] = nums[q.front()];
                l++;
            }
        }

        return res;
    }
};
