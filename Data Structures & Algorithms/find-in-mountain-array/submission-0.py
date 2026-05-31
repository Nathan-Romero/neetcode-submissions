# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        l, r = 0, (n := mountainArr.length() - 1)
        while l < r:
            if mountainArr.get(m := l + (r - l >> 1)) < mountainArr.get(m + 1):
                l = peak = m + 1
            else:
                r = m

        l, r = 0, peak
        while l <= r:
            if (cur := mountainArr.get(m := l + (r - l >> 1))) == target:
                return m
            if cur < target:
                l = m + 1
            else:
                r = m - 1

        l, r = peak, n
        while l <= r:
            if (cur := mountainArr.get(m := l + (r - l >> 1))) == target:
                return m
            if cur > target:
                l = m + 1
            else:
                r = m - 1

        return -1