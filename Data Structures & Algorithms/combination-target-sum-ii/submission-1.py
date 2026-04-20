class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        candidates.sort()
        cur, res = [], []

        def dfs(i, total):
            if total == target:
                res.append(cur[:])
                return

            for j in range(i, n):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue

                if total + candidates[j] > target:
                    return

                cur.append(candidates[j])
                dfs(j + 1, total + candidates[j])
                cur.pop()

        dfs(0, 0)
        return res