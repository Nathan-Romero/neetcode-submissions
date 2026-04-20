from itertools import permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return [[*p] for p in permutations(nums)]