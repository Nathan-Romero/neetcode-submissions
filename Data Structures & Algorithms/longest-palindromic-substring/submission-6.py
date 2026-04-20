class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        start = max_len = 0

        for i in range(n):
            l = r = i

            while l >= 0 and r < n and s[l] == s[r]:
                cur_len = r - l + 1

                if cur_len > max_len:
                    start, max_len = l, cur_len

                l -= 1
                r += 1

            l, r = i, i + 1

            while l >= 0 and r < n and s[l] == s[r]:
                cur_len = r - l + 1

                if cur_len > max_len:
                    start, max_len = l, cur_len

                l -= 1
                r += 1

        return s[start : start + max_len]