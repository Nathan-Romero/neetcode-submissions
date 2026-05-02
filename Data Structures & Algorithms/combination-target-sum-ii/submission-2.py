class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        candidates.sort()
        cur, res = [], []

        def dfs(i, need):
            if not need:
                res.append(cur[:])
                return

            for j in range(i, n):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue

                if need - candidates[j] < 0:
                    return

                cur.append(candidates[j])
                dfs(j + 1, need - candidates[j])
                cur.pop()

        dfs(0, target)
        return res