class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = {}
        
        for i, n in enumerate(nums):
            if target - n in count:
                return [count[target - n], i]
            count[n] = i