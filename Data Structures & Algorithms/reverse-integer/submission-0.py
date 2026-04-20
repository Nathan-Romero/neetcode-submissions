class Solution:
    def reverse(self, x: int) -> int:
        MIN, MAX = -2**31, 2**31 - 1

        res = int(''.join(reversed(str(x)))) if x >= 0 else -int(''.join(reversed(str(x)[1:])))
        return res if MIN <= res <= MAX else 0