class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0

        for i in range(n):
            res += self.countPals(s, i, i, n)
            res += self.countPals(s, i, i + 1, n)

        return res

    def countPals(self, s: str, l: int, r: int, n: int) -> int:
        res = 0

        while l >= 0 and r < n and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1

        return res