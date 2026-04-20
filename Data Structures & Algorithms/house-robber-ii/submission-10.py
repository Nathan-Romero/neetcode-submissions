class Solution:
    def rob(self, nums: List[int]) -> int:
        def robber(houses):
            if len(nums) == 1:
                return nums[0]

            rob1 = rob2 = 0

            for money in houses:
                rob1, rob2 = rob2, max(rob1 + money, rob2)

            return rob2

        return max(robber(nums[:-1]), robber(nums[1:]))