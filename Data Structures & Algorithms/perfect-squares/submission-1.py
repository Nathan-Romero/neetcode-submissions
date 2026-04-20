class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] + [n] * n

        for target in range(1, n + 1):
            for s in range(1, target + 1):
                if target - (square := s * s) < 0:
                    break

                dp[target] = min(dp[target], 1 + dp[target - square])

        return dp[n]