class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = res = sum(weights)

        def can_ship(mid):
            cur, cap = 1, mid

            for w in weights:
                if cap - w < 0:
                    cur += 1
                    if cur > days:
                        return False
                    cap = mid
                cap -= w
            return True

        while l <= r:
            if can_ship(mid := l + (r - l >> 1)):
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1

        return res