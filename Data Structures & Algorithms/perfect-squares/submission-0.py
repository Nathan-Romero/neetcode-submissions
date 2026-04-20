class Solution:
    def numSquares(self, n: int) -> int:
        if (stop := math.sqrt(n)).is_integer():
            return 1

        stop = math.floor(stop)
        squares = [i * i for i in range(1, stop + 1)]
        dp = [0] + [n + 1] * n

        for a in range(1, n + 1):
            for c in squares:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])

        return dp[n]