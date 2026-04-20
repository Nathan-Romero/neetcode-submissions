class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = dp2 = 0
        dp1 = 1
        nums = set(["0", "1", "2", "3", "4", "5", "6"])

        for i in range(n - 1, -1, -1):
            if s[i] != "0":
                dp = dp1

            if i + 1 < n and (s[i] == "1" or s[i] == "2" and s[i + 1] in nums):
                dp += dp2

            dp, dp1, dp2 = 0, dp, dp1

        return dp1