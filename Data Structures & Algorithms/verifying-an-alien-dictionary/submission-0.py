class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order = {c: i for i, c in enumerate(order)}
        return sorted(words, key=lambda w: [order[c] for c in w]) == words