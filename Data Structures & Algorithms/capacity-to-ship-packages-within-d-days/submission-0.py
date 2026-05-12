class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)

        while l < r:
            mid, cur, need = l + r >> 1, 0, 1

            for w in weights:
                if cur + w > mid:
                    need += 1
                    cur = 0
                cur += w

            if need > days:
                l = mid + 1
            else:
                r = mid

        return l