class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []

        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]:
                continue

            for j in range(i + 1, n):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                l, r = j + 1, n - 1

                while l < r:
                    cur_sum = num + nums[j] + nums[l] + nums[r]

                    if cur_sum < target:
                        l += 1

                    elif cur_sum > target:
                        r -= 1

                    else:
                        res.append([num, nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1

                        while nums[l] == nums[l - 1] and l < r:
                            l += 1

                        while nums[r] == nums[r + 1] and l < r:
                            r -= 1

        return res