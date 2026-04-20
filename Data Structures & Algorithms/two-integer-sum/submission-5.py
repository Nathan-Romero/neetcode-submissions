class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        nums: [3,4,5,6]
        target: 7
        '''

        # hash map solution
        seen = dict()
        for i, num in enumerate(nums):
            if target - num in seen:
                return [seen[target - num], i]
            seen[num] = i
        # Time complexity: O(n)
        # Space complexity: O(n)
        
        # # loop through every possible pair (brute force O(n^2))
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         # if sum of two numbers == target
        #             # return the indices

        # # time complexity: O(n^2)
        # # space complexity: O(1)