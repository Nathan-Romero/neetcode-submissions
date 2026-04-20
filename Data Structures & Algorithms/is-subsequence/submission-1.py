class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True

        m, n = len(t), len(s)

        if m < n:
            return False

        i = 0

        for c in t:
            if c == s[i]:
                i += 1

                if i >= n:
                    return True

        return False