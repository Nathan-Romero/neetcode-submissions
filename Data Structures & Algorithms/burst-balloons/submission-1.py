class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        nums = [1] + nums + [1]
        dp = [[0] * (n + 2) for _ in range(n + 2)]

        for l in range(n, 0, -1):
            for r in range(l, n + 1):
                for i in range(l, r + 1):
                    coins = nums[l - 1] * nums[i] * nums[r + 1]
                    coins += dp[l][i - 1] + dp[i + 1][r]
                    dp[l][r] = max(dp[l][r], coins)

        return dp[1][n]


        def dfs(nums):
            if len(nums) == 2:
                return 0

            max_coins = 0

            for i in range(1, len(nums) - 1):
                coins = nums[i - 1] * nums[i] * nums[i + 1]
                coins += dfs(tuple(nums[:i]) + tuple(nums[i + 1:]))
                max_coins = max(max_coins, coins)

            return max_coins

        return dfs(tuple(nums))