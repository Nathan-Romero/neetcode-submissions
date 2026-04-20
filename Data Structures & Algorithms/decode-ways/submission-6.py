class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = defaultdict(int, {n: 1})
        ones = set(["0", "1", "2", "3", "4", "5", "6"])
        res = 0

        for i in range(n - 1, -1, -1):
            if s[i] != "0":
                dp[i] = dp[i + 1]

            if s[i] == "1" or s[i] == "2" and i + 1 < n and s[i + 1] in ones:
                dp[i] += dp[i + 2]

        return dp[0]