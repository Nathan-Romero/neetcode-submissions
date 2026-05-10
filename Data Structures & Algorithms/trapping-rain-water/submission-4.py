class Solution:
    def trap(self, height: List[int]) -> int:
        l_max, r_max = height[l := 0], height[r := len(height) - 1]
        res = 0

        while l < r:
            if l_max < r_max:
                l += 1
                res += (l_max := max(height[l], l_max)) - height[l]
            else:
                r -= 1
                res += (r_max := max(height[r], r_max)) - height[r]

        return res