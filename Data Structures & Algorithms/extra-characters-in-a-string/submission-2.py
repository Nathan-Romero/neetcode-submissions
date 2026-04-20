class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            dp[i] = 1 + dp[i + 1]

            for word in dictionary:
                k = len(word)

                if i + k <= n and s[i : i + k] == word:
                    dp[i] = min(dp[i], dp[i + k])

        return dp[0]