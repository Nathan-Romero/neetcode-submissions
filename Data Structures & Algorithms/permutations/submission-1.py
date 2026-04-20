class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        def dfs(i):
            if i == n:
                res.append(nums[:])
                return

            for j in range(i, n):
                nums[i], nums[j] = nums[j], nums[i]
                dfs(i + 1)
                nums[j], nums[i] = nums[i], nums[j]

        dfs(0)
        return res