class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * n + [True]

        for i in range(n - 1, -1, -1):
            for w in wordDict:
                t = len(w)

                if i + t <= n and s[i : i + t] == w:
                    dp[i] = dp[i + t]

                if dp[i]:
                    break

        return dp[0]