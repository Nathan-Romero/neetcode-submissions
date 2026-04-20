from functools import cache

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMin = curMax = 1

        for num in nums:
            curMax, curMin = max(num * curMax, num * curMin, num), min(num * curMax, num * curMin, num)
            res = max(res, curMax)

        return res