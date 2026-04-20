class Solution:
    def rob(self, nums: List[int]) -> int:
        def robber(houses):
            rob1 = rob2 = 0

            for house in houses:
                rob1, rob2 = rob2, max(rob1 + house, rob2)

            return rob2

        return max(nums[0], robber(nums[:-1]), robber(nums[1:]))