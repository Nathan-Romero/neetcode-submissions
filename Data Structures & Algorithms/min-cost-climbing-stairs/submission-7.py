class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        one, two = cost[-2], cost[-1]

        for i in range(n - 3, -1, -1):
            one, two = cost[i] + min(one, two), one

        return min(one, two)