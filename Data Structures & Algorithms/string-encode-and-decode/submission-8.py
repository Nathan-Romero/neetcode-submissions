from functools import reduce

class Solution:
    def encode(self, strs: List[str]) -> str:
        return reduce(lambda acc, s: acc + 'Ä' + s, strs, '')

    def decode(self, s: str) -> List[str]:
        return s.split('Ä')[1:] if s != '' else []