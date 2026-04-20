from functools import cache

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]

        @cache
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