class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks).most_common()
        mx = freq[0][1]
        return max(len(tasks), (mx - 1) * (n + 1) + sum(c == mx for _, c in freq))