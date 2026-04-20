from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        @cache
        def dfs(i, flag):
            if i >= n or (flag and i == n - 1):
                print(f"i: {i}, flag: {flag}, break")
                return 0

            print(f"i: {i}, flag: {flag}, nums[i]: {nums[i]}")
            return max(dfs(i + 1, flag), nums[i] + dfs(i + 2, flag or i == 0))

        return max(dfs(0, True), dfs(1, False))