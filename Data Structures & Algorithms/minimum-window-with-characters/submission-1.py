class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        t_count, window = Counter(t), defaultdict(int)
        have, need = 0, len(t_count)
        res, resLen = [-1, -1], float("inf")
        l, n = 0, len(s)

        for r in range(n):
            c = s[r]
            window[c] += 1

            if window[c] == t_count[c]:
                have += 1

            while have == need:
                if r - l + 1 < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                window[s[l]] -= 1

                if window[s[l]] < t_count[s[l]]:
                    have -= 1

                l += 1

        l, r = res

        return s[l : r + 1] if resLen != float("inf") else ""