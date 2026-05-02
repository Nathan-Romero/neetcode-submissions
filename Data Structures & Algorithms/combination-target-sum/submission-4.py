class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        cur, res = [], []

        def backtrack(i, need):
            if not need:
                res.append(cur[:])
                return

            if i == n or need < 0:
                return

            cur.append(nums[i])
            backtrack(i, need - nums[i])
            cur.pop()
            backtrack(i + 1, need)

        backtrack(0, target)
        return res