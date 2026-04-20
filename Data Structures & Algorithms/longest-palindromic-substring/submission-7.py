class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        start = max_len = 0

        def longestPal(l, r):
            nonlocal start, max_len

            while l >= 0 and r < n and s[l] == s[r]:
                cur_len = r - l + 1

                if cur_len > max_len:
                    start, max_len = l, cur_len

                l -= 1
                r += 1

        for i in range(n):
            longestPal(i, i), longestPal(i, i + 1)

        return s[start : start + max_len]