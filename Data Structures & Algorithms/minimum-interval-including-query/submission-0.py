class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        n = len(queries)
        res = [float('inf')] * n

        for i in range(n):
            for start, end in intervals:
                if start <= queries[i] <= end:
                    res[i] = min(res[i], end - start + 1)

                if res[i] == 1:
                    break

            if res[i] == float('inf'):
                res[i] = -1

        return res