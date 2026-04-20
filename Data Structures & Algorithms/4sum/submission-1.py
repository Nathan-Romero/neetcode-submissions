class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        return k_sum(sorted(nums), target, 4)


def k_sum(nums: List[int], target: int, k: int) -> List[List[int]]:
    if not nums:
        return []

    avg = target // k

    if nums[0] > avg or nums[-1] < avg:
        return []

    if k == 2:
        return two_sum(nums, target)

    res = []

    for i, num in enumerate(nums):
        if not i or nums[i - 1] != num:
            for subset in k_sum(nums[i + 1 :], target - num, k - 1):
                res.append([num] + subset)

    return res


def two_sum(nums: List[int], target: int) -> List[List[int]]:
    l, r = 0, len(nums) - 1
    res = []

    while l < r:
        cur_sum = nums[l] + nums[r]

        if cur_sum < target:
            l += 1

        elif cur_sum > target:
            r -= 1

        else:
            res.append([nums[l], nums[r]])
            l += 1
            r -= 1

            while nums[l] == nums[l - 1] and l < r:
                l += 1

            while nums[r] == nums[r + 1] and l < r:
                r -= 1

    return res