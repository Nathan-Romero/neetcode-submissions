class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        limit = len(nums) // 3
        return [num for num, cnt in Counter(nums).items() if cnt > limit]