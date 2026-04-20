from functools import reduce

class Solution:
    def encode(self, strs: List[str]) -> str:
        return reduce(lambda acc, s: acc + str(len(s)) + "#" + s, strs, "")

    def decode(self, s: str) -> List[str]:
        n = len(s)
        i = 0
        res = []

        while i < n:
            j = i + 1

            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])

            i = j

        return res