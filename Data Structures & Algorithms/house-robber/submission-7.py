class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n <= 2:
            return max(nums)

        dp = [0] * n
        dp[-1], dp[-2] = nums[-1], nums[-2]

        for i in range(n - 3, -1, -1):
            dp[i] = max(dp[i + 1], nums[i] + dp[i + 2])

        return dp[0]