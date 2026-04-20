class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        l, r = 0, n - 1

        while l < r:
            cur = nums[l] + nums[r]

            if cur < target:
                l += 1

            elif cur > target:
                r -= 1

            else:
                return [l + 1, r + 1]