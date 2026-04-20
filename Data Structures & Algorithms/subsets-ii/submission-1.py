class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        subset, res = [], []

        def dfs(i):
            res.append(subset[:])

            for j in range(i, n):
                if j > i and nums[j] == nums[j - 1]:
                    continue

                subset.append(nums[j])
                dfs(j + 1)
                subset.pop()

        dfs(0)
        return res