class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n

        for i in range(n - 1):
            cur = 0

            for j in range(i + 1, n):
                cur += 1

                if temperatures[j] > temperatures[i]:
                    res[i] = cur
                    break

        return res