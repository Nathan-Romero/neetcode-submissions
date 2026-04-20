from operator import sub

class Solution:
    def scoreOfString(self, s: str) -> int:
        return sum(starmap(lambda x, y: abs(ord(y) - ord(x)), pairwise(s)))