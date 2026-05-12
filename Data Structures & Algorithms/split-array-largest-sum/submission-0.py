class Solution:

    def helper(self, nums: List[int], perK: int, k: int) -> bool:
        cur, count = 0, 1

        for num in nums:
            if cur + num > perK:
                count += 1
                cur = num

            else:
                cur += num

        return count <= k

    def splitArray(self, nums: List[int], k: int) -> int:
        l, r = max(nums), sum(nums)
        res = 0

        while l <= r:
            mid = l + (r - l >> 1)

            if self.helper(nums, mid, k):
                res = mid
                r = mid - 1

            else:
                l = mid + 1

        return res