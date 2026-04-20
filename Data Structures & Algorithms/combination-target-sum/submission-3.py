from itertools import combinations_with_replacement

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        return [[*c] for r in range(1, target + 1) for c in combinations_with_replacement(nums, r) if sum(c) == target]