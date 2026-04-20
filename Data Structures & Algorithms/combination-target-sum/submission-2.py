from itertools import combinations_with_replacement

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res = []

        for i in range(1, target):
            combos = [list(c) for c in combinations_with_replacement(nums, i) if sum(c) == target]

            if combos:
                res.extend(combos)

        return res