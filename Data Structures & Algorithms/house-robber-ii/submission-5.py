from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        @cache
        def dfs(i, flag):
            if i >= n or (flag and i == n - 1):
                return 0

            return max(dfs(i + 1, flag), nums[i] + dfs(i + 2, flag))

        return max(dfs(0, True), dfs(1, False))