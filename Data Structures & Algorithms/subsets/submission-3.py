from itertools import combinations

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return [[*c] for r in range(len(nums) + 1) for c in combinations(nums, r)]