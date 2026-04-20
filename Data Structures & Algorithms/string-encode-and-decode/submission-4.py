from functools import reduce

class Solution:
    def encode(self, strs: List[str]) -> str:
        return reduce(lambda acc, s: acc + str(len(s)) + "#" + s, strs, "")

    def decode(self, s: str) -> List[str]:
        n = len(s)
        l, r = 0, 1
        res = []

        while r < n:
            if s[r] != "#":
                r += 1

            else:
                length = int(s[l:r])
                l = r + 1
                r = l + length
                res.append(s[l:r])

                l = r
                r += 1

        return res