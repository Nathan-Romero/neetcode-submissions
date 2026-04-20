class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        print(f'{dp}\n')

        for i in range(n - 2, -1, -1):
            print(f'i: {i}')
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
                    print(f'j: {j}, dp: {dp}')

            print()

        return max(dp)