class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n = len(arr)
        res = 0
        curSum = sum(arr[:k - 1])

        for l in range(n - k + 1):
            curSum += arr[l + k - 1]

            if (curSum / k) >= threshold:
                res += 1

            curSum -= arr[l]

        return res