class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((w, v))

        visited = set()
        minHeap = [(0, k)]
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            visited.add(n1)

            if len(visited) == n:
                return w1

            for w2, n2 in adj[n1]:
                if not n2 in visited:
                    heapq.heappush(minHeap, (w1 + w2, n2))

        return -1