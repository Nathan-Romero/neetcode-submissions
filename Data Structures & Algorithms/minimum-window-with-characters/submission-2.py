class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count, window = Counter(t), defaultdict(int)
        have, need = 0, len(t_count)
        rl = rr = -1
        l, n = 0, len(s)

        for r in range(n):
            c = s[r]
            window[c] += 1

            if window[c] == t_count[c]:
                have += 1

            while have == need:
                if rl < 0 or r - l + 1 < rr - rl + 1:
                    rl, rr = l, r

                window[s[l]] -= 1

                if window[s[l]] < t_count[s[l]]:
                    have -= 1

                l += 1

        return s[rl : rr + 1] if rl != -1 else ""