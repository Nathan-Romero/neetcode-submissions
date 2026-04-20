from itertools import permutations

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return list(set([tuple(p) for p in permutations(nums)]))