from functools import cache

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        @cache
        def backtrack(i, total):
            if i == n:
                return total == target

            return (backtrack(i + 1, total + nums[i]) +
                    backtrack(i + 1, total - nums[i]))

        return backtrack(0, 0)